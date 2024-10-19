

from DrissionPage import ChromiumPage

from colorama import Fore, init
import time


def packet_tree(packet,to_expand='response'):

    def _tree(obj, last_one=True, body='', level=0):
        if obj is None:
            return 1
        
        obj = obj[0] if isinstance(obj, list) and len(obj) !=0 else obj
        if type(obj).__name__=='CaseInsensitiveDict':
            obj=dict(obj)
            pass


        is_dict = isinstance(obj, (dict,))
        not_dict = not is_dict  

        
        show_len = 150
        list_ele = [i for i in dir(obj) if not i.startswith('_')]  if not_dict else obj.keys()

        length = len(list_ele)
        body_unit = '    ' if last_one else '│   '
        tail = '├───'
        new_body = body + body_unit

        if length > 0:
            new_last_one = False
            
            for idx, attr_name in enumerate(list_ele):
                if idx == length - 1:
                    tail = '└───'
                    new_last_one = True
                   
                try:
                    packet_attr = getattr(obj, attr_name) if not_dict else obj[attr_name]
                except:
                    print(f'{attr_name} {obj}  出错！')
                    continue
                
                packet_attr_type = type(packet_attr).__name__
                if    packet_attr_type=='method':
                    continue

                value = str(packet_attr).split('\n')[0][:show_len]  

                # 打印属性信息
                # attr_name=attr_name.ljust(15)
                if packet_attr_type != 'builtin_function_or_method' : 
                        if packet_attr_type=='dict':
                             print(f'{new_body}{tail}< {Fore.BLUE}{attr_name}{Fore.RESET} {Fore.RED}{packet_attr_type}{Fore.RESET}  ')
                        else:
                            if is_dict:
                                print(f'{new_body}{tail}# {Fore.GREEN}{attr_name}{Fore.RESET} {Fore.RED}{packet_attr_type}{Fore.RESET}  {value}')
                            else:
                                print(f'{new_body}{tail}< {Fore.BLUE}{attr_name}{Fore.RESET} {Fore.RED}{packet_attr_type}{Fore.RESET}  {value}')


      

                # 递归处理特定属性
                if attr_name in fields_to_expand or packet_attr_type in types_to_expand :
                    _tree(packet_attr, new_last_one, new_body, level + 1)
               




    init()
    # fields_to_expand=['response', 'request', 'body', 'headers', 'values','get']
    fields_to_expand=['get']
    fields_to_expand.append(to_expand)
    types_to_expand=['dict','list']

    print(f'{Fore.YELLOW}{packet}{Fore.RESET}')
    _tree(packet)         
            
                    


page = ChromiumPage()
page.listen.start('.jpg')  # 开始监听，指定获取包含该文本的数据包
page.get('https://book.douban.com/')  # 访问网址


i = 0
for packet in page.listen.steps():
    print('\n'*3)  # 打印数据包url    
    packet_tree(packet)
    # print(packet.request.cookies)
    # break
    
    
