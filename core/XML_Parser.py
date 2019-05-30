from core.config.paths import root_path
from core.config.paths import input_path
from core.config.paths import output_path
from core.helper.ProducerConsumerThread import ProducerThread
from core.helper.ProducerConsumerThread import ConsumerThread
from core.helper.XML_Traverse import output_csv
import xml.etree.ElementTree as ET
import os


class XML_Parser:

    def __init__(self,input_file, output_file, element):
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
        self.element_list = list()

    def parse_xml(self):
        """

        :return:
        """
        it = ET.iterparse(os.path.join(self.input_path, self.input_file))
        for _, el in it:
            if '}' in el.tag:
                el.tag = el.tag.split('}', 1)[1]  # strip all namespaces
        root = it.root
        if root.find('{}{}'.format('.//', self.element)) is None:
            raise ValueError('{} -- Invalid node Element. Please enter a valid Element to parse'.format(self.element))
        else:
            for element in root.iter(self.element):
                self.element_list.append(element)


    def processing(self):
        """

        :return:
        """
        total_element = len(self.element_list)
        p1 = ProducerThread(self.element_list)
        producer_thread_list = list()
        producer_thread_list.append(p1)
        consumer_thread_list = [ConsumerThread(total_element) for x in range(100)]
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
        self.parse_xml()
        self.processing()
        output_csv(self.output_path, self.output_file)