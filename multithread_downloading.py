import threading
import urllib
from urllib import request
import socket, os

'''
    This is a multithreading movie downloader.

    Software: MT_Downloader
    Author: ItiharaYuuko
    Time: 04_29_2020
    E-mail: wert3714@yahoo.com
    Version: 0.3.1_Beta
'''

class BaseThread (threading.Thread):

    '''
        Support the multithreadings class.
        Initialize the class with five
        parameters: 
            1.thread_id: an integer for the new thread tag;
            2.thread_name: a string for the new thread name;
            3.args_pass: a structured data for the mulitithreads,
                        whatever using the unit, array, dictionary.
                        Able to transfer the data from super function;
            4.start_nu: the begining of the multithreads range mark;
            5.end_nu: the ending of the multithreads range mark;
    '''

    def __init__(self, thread_id,
                thread_name,
                args_pass,
                start_nu,
                end_nu):

        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.args_pass = args_pass
        self.start_nu = start_nu
        self.end_nu = end_nu

    def auto_down(self, url, filename):
        
        '''
            The major of the download function,
            the first parameter is targets 'url',
            the second parameter is targets files
            storage path on your harddisk.
        '''

        try:
            request.urlretrieve(url, filename)
        except urllib.error.URLError as err:
            print(err.reason)
            self.auto_down(url,filename)

    def run(self):
        
        '''
            The methord will running when the threading modules
            methord 'start()' called.
        '''

        print('id = %s, name = %s' % 
                (self.thread_id, self.thread_name))

        for i in range(self.start_nu, self.end_nu):
            request.urlcleanup()
            tempFileNum = 'film_%05d' % i
            tempFileName = '%s.%s' % (tempFileNum,self.args_pass.get('files_type'))
            print('Downloading: %s' % tempFileName)
            try:
                self.auto_down(self.args_pass.get('url') + tempFileName,
                                self.args_pass.get('files_path') + tempFileName)
            except socket.timeout:
                self.auto_down(self.args_pass.get('url') + tempFileName,
                                self.args_pass.get('files_path') + tempFileName)

            print('%s downloaded successed.' % tempFileName)



if __name__ == "__main__":

    usage_information = {'files_count': 1137,
                    'url': 'https://cn4.sxylcy.cc/hls/20190713/9237d3aee163854ee222a5ec1c356245/1563018087/',
                    'files_type': 'ts',
                    'files_path': 'I:\\Documents and Settings\\TDDownload\\afzz\\'}

    #The 'usage_information' variable is information which movie you want to downloading.
    #data structures type is dictionary.

    thread_id_count = 0
    st = 100
    #The 'st' variable is step of the ergodic, it controling the
    #numbers of threads. 
    subs = 0
    for i in range(0, usage_information.get('files_count'), st):
        thread_id_count += 1
        if i != 0:
            if i - st != 0:
                start_num = i - st
                end_num = i
                thna = 'T-%d' % thread_id_count
                threadx = BaseThread(thread_id_count,
                                    thna,
                                    usage_information,
                                    start_num, end_num)
                threadx.start()
            else:
                start_num = i - st
                end_num = i
                thna = 'T-%d' % thread_id_count
                threadx = BaseThread(thread_id_count,
                                    thna,
                                    usage_information,
                                    start_num, end_num)
                threadx.start()
        subs = i

    thread_id_count += 1
    start_num = subs
    end_num = usage_information.get('files_count')
    thna = 'T-%d' % thread_id_count
    threadx = BaseThread(thread_id_count,
                        thna,
                        usage_information,
                        start_num, end_num)

    threadx.start()