import json
import logging
import boto3
from botocore.exceptions import ClientError
from typing import Callable, Any, Dict
from concurrent.futures import ThreadPoolExecutor
import threading

logging.getLogger().setLevel(logging.INFO)


class AWSDataBus:
    """
    An EventBridge and SQS interface class to handle event-driven communication.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AWSDataBus, cls).__new__(cls)
        return cls._instance

    def __init__(self, config: Dict = None):
        """
        Initialize the AWSDataBus and start listening to the SQS queue.
        Args:
            config (Dict): A dictionary containing the EventBridge and SQS configuration.
        """
        if not hasattr(self, "initialized"):  # Prevent reinitialization
            super().__init__()
            self.eventbridge = boto3.client('events')
            self.sqs = boto3.client('sqs')
            self.event_bus_name = config.get('event_bus_name')
            self.queue_url = config.get('queue_url')
            self.queue_arn = config.get("queue_arn")
            self.source_name = config.get("source_name")
            self.callback_registry = {}  # Store callbacks for subscribed events
            self.initialized = True
            self.stop_event = threading.Event()

            if self.queue_url:
                # Start listening to the SQS queue as soon as initialized in a thread pool
                self.executor = ThreadPoolExecutor(max_workers=4)
                self.executor.submit(self._start_listening)

    def subscribe_async_event(self, event_name: str, callback: Callable[[Any], None]):
        """
        Subscribe to an event by creating an EventBridge rule and store the callback for the event.
        Args:
            event_name (str): The name of the event to subscribe to.
            event_pattern (str): The event pattern for filtering events.
            callback (Callable[[Any], None]): The callback function to be invoked when the event is received.
        """
        rule_name = f'{event_name}_{self.source_name}_rule'
        event_pattern = json.dumps(
            {
                "detail-type": [event_name],
            }
        )
        try:
            # Create EventBridge Rule
            self.eventbridge.put_rule(
                Name=rule_name,
                EventPattern=event_pattern,
                State='ENABLED',
                EventBusName=self.event_bus_name
            )
            logging.info(f"Event rule '{rule_name}' created.")

            # Add SQS queue as target
            self.eventbridge.put_targets(
                Rule=rule_name,
                EventBusName=self.event_bus_name,
                Targets=[
                    {
                        "Id": f"{event_name}_sqs_target",
                        "Arn": self.queue_arn,  # SQS queue ARN
                    }
                ],
            )
            logging.info(f"SQS queue target added to rule '{rule_name}'.")

            # Register the callback for the event
            self.callback_registry[event_name] = callback
            logging.info(f"Callback registered for event '{event_name}'.")

        except ClientError as e:
            logging.error(f"Failed to subscribe to event '{event_name}': {e}")

    def _start_listening(self):
        """
        Start listening to the SQS queue and process messages using the stored callbacks in a thread.
        """
        logging.info(f"Listening to SQS queue '{self.queue_url}' for messages...")

        while not self.stop_event.is_set():
            try:
                # Poll SQS queue for messages
                response = self.sqs.receive_message(
                    QueueUrl=self.queue_url,
                    MaxNumberOfMessages=10,
                    WaitTimeSeconds=20
                )
                messages = response.get('Messages', [])
                for message in messages:
                    logging.info(f"Received message from SQS: {message}")
                    self._process_message(message)
                    # Delete the message from the queue after processing
                    # self.delete_message(message['ReceiptHandle'])
            except ClientError as e:
                logging.error(f"Error receiving message from SQS: {e}")

    def _process_message(self, message: Dict):
        """
        Process an incoming message and invoke the registered callback for the event.
        Args:
            message (Dict): The message received from the SQS queue.
        """
        try:
            body = json.loads(message['Body'])
            event_name = body.get('detail-type')

            # Check if a callback is registered for the event
            if event_name in self.callback_registry:
                callback = self.callback_registry[event_name]
                logging.info(f"Invoking callback for event '{event_name}' with message body: {body}")
                callback(message)
            else:
                logging.warning(f"No callback registered for event '{event_name}'.")
        except Exception as e:
            logging.error(f"Error processing message: {e}")

    def publish_event(self, event_name: str, event_payload: dict):
        """
        Publish an event to the EventBridge.
        Args:
            event_name (str): The name of the event to publish.
            event_payload (dict): The payload of the event.
        Returns:
            bool: True if the event was published successfully.
        """
        try:
            response = self.eventbridge.put_events(
                Entries=[
                    {
                        "Source": self.source_name,
                        "DetailType": event_name,
                        "Detail": json.dumps(event_payload),
                        "EventBusName": self.event_bus_name,
                    }
                ]
            )
            logging.info(f"Published event '{event_name}': {event_payload}, response: {response}")
            return True
        except ClientError as e:
            logging.error(f"Failed to publish event: {e}")
            return False

    def delete_message(self, receipt_handle: str):
        """
        Delete a message from the SQS queue.
        Args:
            receipt_handle (str): The receipt handle associated with the message to delete.
        """
        try:
            self.sqs.delete_message(
                QueueUrl=self.queue_url,
                ReceiptHandle=receipt_handle
            )
            logging.info(f"Message deleted from SQS queue with receipt handle '{receipt_handle}'.")
        except ClientError as e:
            logging.error(f"Failed to delete message from SQS: {e}")
