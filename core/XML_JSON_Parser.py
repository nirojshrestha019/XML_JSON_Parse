from core.config.paths import root_path
from core.config.paths import input_path
from core.config.paths import output_path
from core.helper.ProducerConsumerThread import ProducerThread
from core.helper.ProducerConsumerThread import ConsumerThread
from core.helper.XML_JSON_Traverse import output_csv
import xml.etree.ElementTree as ET
import os
import json


class XmlJsonParser:
    def __init__(self, input_file, output_file, element):
        """

        :param input_file:
        :param output_file:
        :param element:
        """
        self.root_path = root_path
        self.input_path = input_path
        self.output_path = output_path
        self.input_file = input_file
        self.output_file = output_file
        self.element = element
        self.input_file_type = self.input_file.split(".")[-1]
        self.element_list = list()

    def file_read(self):
        """

        :return:
        """
        if self.input_file_type == "xml":
            it = ET.iterparse(os.path.join(self.input_path, self.input_file))
            for _, el in it:
                if "}" in el.tag:
                    el.tag = el.tag.split("}", 1)[1]  # strip all namespaces
            root = it.root
            if root.find("{}{}".format(".//", self.element)) is None:
                raise ValueError(
                    "{} -- Invalid node Element. Please enter a valid Element to parse".format(
                        self.element
                    )
                )
            else:
                for element in root.iter(self.element):
                    self.element_list.append(element)

        elif self.input_file_type == "json":
            fp = open(os.path.join(self.input_path, self.input_file), "r")
            json_value = fp.read()
            raw_data = json.loads(json_value)
            fp.close()
            try:
                self.element_list = raw_data[self.element]
            except:
                self.element_list = raw_data

        else:
            raise Exception("Invalid File format.")

    def processing(self):
        """

        :return:
        """
        total_element = len(self.element_list)
        p1 = ProducerThread(self.element_list)
        producer_thread_list = list()
        producer_thread_list.append(p1)
        consumer_thread_list = [
            ConsumerThread(total_element, self.input_file_type, self.element)
            for x in range(100)
        ]
        for each_producer in producer_thread_list:
            each_producer.start()
        for each_consumer in consumer_thread_list:
            each_consumer.start()
        for each_producer in producer_thread_list:
            each_producer.join()
        for each_consumer in consumer_thread_list:
            each_consumer.join()

    def start(self):
        """

        :return:
        """
        self.file_read()
        self.processing()
        output_csv(self.output_path, self.output_file)
