from threading import Thread
from queue import Queue
from core.helper.XML_JSON_Traverse import parse_from_root

queue = Queue(150)


class ProducerThread(Thread):
    def __init__(self, element_list):
        """

        :param element_list:
        """
        super(ProducerThread, self).__init__()
        self.element_list = element_list

    def run(self):
        """

        :return:
        """
        global queue
        while self.element_list:
            each_item = self.element_list.pop()
            queue.put(each_item)


class ConsumerThread(Thread):
    def __init__(self, total_element, input_file_type, element):
        """

        :param total_element:
        """
        super(ConsumerThread, self).__init__()
        self.total_element = total_element
        self.input_file_type = input_file_type
        self.element = element

    def run(self):
        """

        :return:
        """
        global queue
        while not queue.empty():
            each_item = queue.get()
            parse_from_root(
                each_item, self.total_element, self.input_file_type, self.element
            )
            queue.task_done()
