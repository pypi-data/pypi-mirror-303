import json
from urllib.parse import unquote
from agent.utils.nacos_val import get_system_config_from_nacos
from agent.fegin.portal_client import PortalClient
from agent.utils.dde_logger import format_log


class MemoryService:
    def __init__(self, logger, portal_address, system_config):
        self.logger = logger
        self.portal_client = PortalClient(logger, portal_address, system_config)

    # 检查当前轮对话是否上传pdf文档
    def check_last_contain_pdf(self, data):
        second_last_element = data[-2]
        if 'resourceList' in second_last_element:
            resource_list = second_last_element['resourceList']
            if resource_list:
                for item in resource_list:
                    if '.pdf' in item.lower():
                        return True
        return False

    # 获取history中最后一个pdf文档的index
    def find_last_pdf_order_index(self, data):
        # 查找包含 PDF 类型的最后一个文档的 orderIndex
        last_pdf_order_index = None
        for message in reversed(data):
            if 'resourceList' in message and message['resourceList']:
                for resource in message['resourceList']:
                    if '.pdf' in resource.lower():
                        last_pdf_order_index = message['orderIndex']
                        break
            if last_pdf_order_index:
                break
        return last_pdf_order_index

    # 获取完整的memory信息，包括所使用的工具
    def retrieve_complete_memory(self, session_id: str, max_round: int = 20, max_length: int = 4000, remove_current_chat: bool = True):
        self.logger.info(f'根据session_id[%s]从portal后端查询retrieve_complete_memory', session_id)
        memories = []
        try:
            memory_resp = self.portal_client.get_chat_detail(session_id)
            if memory_resp is None or memory_resp.get("data") is None or memory_resp.get("data").get("conversation") is None:
                self.logger.info(f'根据session_id[%s]从portal后端查询历史消息为空，请检查参数', session_id)
                self.logger.info(f'retrieve_memory,session_id[{session_id}],return[]')
                return []
            chat_info_list = memory_resp.get('data').get('conversation')
            self.logger.info(f'根据session_id[{session_id}]从portal后端查询retrieve_complete_memory, chat_info_list:{json.dumps(chat_info_list)}')
            if len(chat_info_list) < 2:
                self.logger.info(f"retrieve_complete_memory,len(chat_info_list) < 2, return[],session_id={session_id}")
                self.logger.info(f'retrieve_complete_memory,session_id[{session_id}],return[]')
                return []
            if remove_current_chat:
                chat_info_list = chat_info_list[:-2]
                self.logger.info(f'session_id[{session_id}], remove_current_chat is true, remove last 2 chat_info')
            memory_length = 0
            memory_round = 0
            for i in range(len(chat_info_list) - 1, -1, -2):
                if max_round > 0 and memory_round >= max_round:
                    self.logger.info(f'当前历史对话轮数超过{max_round}轮,不再新增历史对话,session_id[{session_id}]')
                    break
                chat_memory = {}
                if chat_info_list[i - 1]['text'] is None or chat_info_list[i]['text'] is None:
                    continue
                chat = chat_info_list[i - 1]["text"]
                chat = chat.replace("\\n", "\n")
                chat_memory.update({"question": chat, "chatId": chat_info_list[i - 1]["chatId"]})
                files = []
                if len(chat_info_list[i - 1]["resourceList"]) > 0:
                    for resource in chat_info_list[i - 1]["resourceList"]:
                        data = json.loads(resource)
                        files.append(data['url'])
                chat_memory.update({'files': files})
                plugin = chat_info_list[i]["pluginCode"]
                is_reference = True
                if "Web Search" in plugin:
                    is_reference = False
                content = self.retrieve_content_from_answer(chat_info_list[i]['text'], is_reference)
                #content = content.replace("\\n", "\n").replace('\n\n','\n')
                content = content.replace("\\n", "\n")
                chat_memory.update({"answer": content})
                chat_memory.update({"plugin": plugin})
                memory_length = memory_length + len(json.dumps(chat_memory))
                format_log(_type="00_log", content=f"检索构造memory,当前轮次[{str(memory_round)}]的长度为[{str(memory_length)}],当前轮次的chat_memory为[{str(chat_memory)}]")
                if max_length > 0 and memory_length >= max_length:
                    self.logger.info(f'当前历史对话字符长度超过{max_length},不再新增历史对话,session_id[{session_id}]')
                    break
                memories.insert(0, chat_memory)
                format_log(_type="00_log", content=f"检索构造memory,当前轮次[{str(memory_round)}]的长度为[{str(memory_length)}],当前轮次的chat_memory为[{str(chat_memory)}],总的memories为[{str(memories)}]")
                memory_round = memory_round + 1
        except Exception as e:
            self.logger.error("获取历史消息时，发生%s异常", str(e), exc_info=True)
        self.logger.info(f'retrieve_complete_memory,session_id[{session_id}],return[{memories}]')
        return memories

    # def retrieve_complete_memory_without_discard_keyword_for_rag(self, session_id, remove_current_chat=True):
    #     system_config = get_system_config_from_nacos()
    #     max_count = system_config["feign"]["memory_control"]["max_count"]
    #     max_byte = system_config["feign"]["memory_control"]["max_byte"]  # 暂时用字节数控制长度，后续考虑优化成token数
    #     consider_latest_intent_count = system_config["feign"]["memory_control"]["consider_latest_intent_count"]
    #     new_memories = self.retrieve_complete_memory_without_discard_keyword( session_id, max_count, max_byte, remove_current_chat)
    #     result = []
    #     # 去掉上一个工具之前的history（保留 consider_latest_intent_count 轮）
    #     if consider_latest_intent_count < 0:
    #         for memory in new_memories:
    #             result.append([memory["question"], memory["answer"]])
    #         return result
    #     else:
    #         last_intent = None
    #         count = 0
    #         for i in range(len(new_memories) - 1, -1, -1):
    #             this_memory = new_memories[i]
    #             if this_memory["plugin"] == "General Chat" or this_memory["plugin"] == "":
    #                 if last_intent is None:
    #                     result.insert(0, [this_memory["question"], this_memory["answer"]])
    #                     continue
    #                 else:
    #                     break
    #             else:
    #                 if last_intent is None:
    #                     if consider_latest_intent_count <= 0:
    #                         break
    #                     else:
    #                         count = count + 1
    #                         last_intent = this_memory["plugin"]
    #                         result.insert(0, [this_memory["question"], this_memory["answer"]])
    #                 else:
    #                     if this_memory["plugin"] != last_intent:
    #                         break
    #                     elif count >= consider_latest_intent_count:
    #                         break
    #                     else:
    #                         count = count + 1
    #                         result.insert(0, [this_memory["question"], this_memory["answer"]])
    #     return result


    def retrieve_complete_memory_without_discard_keyword(self, session_id: str, max_round: int = 20, max_length: int = 4000, remove_current_chat: bool = True, rag_switch: str = "off"):
        '''
          根据sessionId检索memory，并且去掉需要移除的历史消息，例如，Sorry, no content was returned due to exception
        '''
        self.logger.info(f'根据session_id[{session_id}]从portal后端查询所有memory,丢弃被排除的关键字', )
        chat_history =[]
        try:
            memories = self.retrieve_complete_memory(session_id, max_round, max_length, remove_current_chat)
            system_config = get_system_config_from_nacos()
            discard_kw = system_config["feign"]["memory_control"]["discard_kw"]
            for i in range(len(memories) - 1, -1, -1):
                this_memory = memories[i]
                if any(kw.lower() in this_memory["answer"].lower() for kw in discard_kw):
                    continue
                chat_history.insert(0, [this_memory["question"], this_memory["answer"]])
            format_log(_type="00_log", content=f'根据sessionId[{session_id}]查得memory[{memories}],拆解完成后得到的memory为[{chat_history}]')
            if rag_switch != "off":
                format_log(_type="00_log", content=f'根据sessionId[{session_id}]查得memory[{memories}], 传入的rag_switch为[{rag_switch}],需要进行rag处理')
                for i, (key, answer) in enumerate(chat_history):
                    if answer is not None and answer != '':
                        index = answer.find('[')
                        new_answer = answer[:index]
                        chat_history[i] = (key, new_answer)
                format_log(_type="00_log", content=f'根据sessionId[{session_id}]查得memory[{memories}], 传入的rag_switch为[{rag_switch}],需要进行rag处理,经过rag处理后结果为[{chat_history}]')
        except Exception as e:
            self.logger.error("获取历史消息时，发生%s异常", str(e), exc_info=True)
        self.logger.info(f'retrieve_complete_memory_without_discard_keyword,session_id[{session_id}],return[{chat_history}]')
        return chat_history
    def retrieve_complete_memory_question(self, session_id: str, max_round: int = 20, max_length: int = 4000, remove_current_chat: bool = True):
        self.logger.info(f'根据session_id[{session_id}]从portal后端查询历史记录中的问题部分 retrieve_complete_memory_question')
        memories = []
        try:
            memory_resp = self.portal_client.get_chat_detail(session_id)
            if memory_resp is None or memory_resp.get("data") is None or memory_resp.get("data").get("conversation") is None:
                self.logger.info(f'根据session_id[%s]从portal后端查询历史记录中的问题部分,返回数据为空,请检查参数', session_id)
                self.logger.info(f'retrieve_complete_memory_question,session_id[{session_id}],return[]')
                return []
            chat_info_list = memory_resp.get('data').get('conversation')
            self.logger.info(f'根据session_id[{session_id}]从portal后端查询历史记录中的问题部分 retrieve_complete_memory_question, chat_info_list:{json.dumps(chat_info_list)}')
            if len(chat_info_list) < 2:
                self.logger.info(f"retrieve_complete_memory_question,len(chat_info_list) < 2, return[],session_id={session_id}")
                self.logger.info(f'retrieve_complete_memory_question,session_id[{session_id}],return[]')
                return []
            if remove_current_chat:
                chat_info_list = chat_info_list[:-2]
                self.logger.info(f'session_id[{session_id}],retrieve_complete_memory_question, remove_current_chat is true, remove last 2 chat_info')
            memory_length = 0
            memory_round = 0
            for i in range(len(chat_info_list) - 1, -1, -2):
                if max_round > 0 and memory_round >= max_round:
                    self.logger.info(f'retrieve_complete_memory_question,当前历史对话轮数超过{max_round}轮,不再新增历史对话,session_id[{session_id}]')
                    break
                chat_memory = {}
                if chat_info_list[i - 1]['text'] is None or chat_info_list[i]['text'] is None:
                    continue
                chat = chat_info_list[i - 1]["text"]
                chat = chat.replace("\\n", "\n")
                chat_memory.update({"question": chat, "chatId": chat_info_list[i - 1]["chatId"]})

                plugin = chat_info_list[i]["pluginCode"]
                chat_memory.update({"answer": ""})
                chat_memory.update({"plugin": plugin})
                if max_length > 0 and memory_length >= max_length:
                    self.logger.info(f'retrieve_complete_memory_question,当前历史对话字符长度超过{max_length},不再新增历史对话,session_id[{session_id}]')
                    break
                memories.insert(0, chat_memory)
                format_log(_type="00_log", content=f"检索构造retrieve_complete_memory_question,当前轮次[{str(memory_round)}]的长度为[{str(memory_length)}],当前轮次的chat_memory为[{str(chat_memory)}],总的memories为[{str(memories)}]")
                memory_round = memory_round + 1
        except Exception as e:
            self.logger.error("retrieve_complete_memory_question,获取历史消息时，发生%s异常", str(e), exc_info=True)
        self.logger.info(f'retrieve_complete_memory_question,session_id[{session_id}],return[{memories}]')
        return memories

    def retrieve_memory(self, session_id: str, split_pdf: bool = False):
        self.logger.info(f'根据session_id[%s]从portal后端查询历史消息, split_pdf=[%s]', session_id, split_pdf)
        memories = []
        try:
            memory_resp = self.portal_client.get_chat_detail(session_id)
            if memory_resp is None or memory_resp.get("data") is None or memory_resp.get("data").get("conversation") is None:
                self.logger.info(f'根据session_id[%s]从portal后端查询历史消息为空，请检查参数', session_id)
                self.logger.info(f'retrieve_memory,session_id[{session_id}],return[]')
                return []
            chat_info_list = memory_resp.get('data').get('conversation')
            if len(chat_info_list) < 2:
                self.logger.info(f"retrieve_memory,len(chat_info_list) < 2, return[],session_id={session_id}")
                self.logger.info(f'retrieve_memory,session_id[{session_id}],return[]')
                return []
            # 如果本轮对话上传了pdf，则不传history
            if self.check_last_contain_pdf(chat_info_list):
                self.logger.info(f"chat contain pdf, return[],session_id={session_id}")
                self.logger.info(f'retrieve_memory,session_id[{session_id}],return[]')
                return []
            chat_info_list = chat_info_list[:-2]
            if split_pdf:
                # 对于文献解析，本轮没有上传pdf，则需要清除上一个pdf之前的history
                last_pdf_index = self.find_last_pdf_order_index(chat_info_list)
                if last_pdf_index is not None:
                    chat_info_list = chat_info_list[last_pdf_index:]
            num = 0
            memory_length = 0
            for i in range(0, len(chat_info_list), 2):
                chat_memory = []
                if chat_info_list[i]['text'] is not None and chat_info_list[i + 1]['text'] is not None:
                    chat = chat_info_list[i]["text"]
                    chat = chat.replace("\\n", "\n")
                    chat_memory.append(chat)
                    content = self.retrieve_content_from_answer(chat_info_list[i + 1]['text'])
                    content = content.replace("\\n", "\n")
                    chat_memory.append(content)
                    memories.append(chat_memory)
                num += 1
                if chat_memory is not None:
                    memory_length = memory_length + len(chat_memory)
                if num >= 20:
                    self.logger.info(f'当前历史对话轮数超过20轮,不再新增历史对话,session_id[{session_id}]')
                    break
                if memory_length >= 4000:
                    self.logger.info(f'当前历史对话字符长度超过4000,不再新增历史对话,session_id[{session_id}]')
                    break
        except Exception as e:
            self.logger.error("获取历史消息时，发生%s异常", str(e), exc_info=True)
        self.logger.info(f'retrieve_memory,session_id[{session_id}],return[{memories}]')
        return memories

    def retrieve_content_from_answer(self, content, is_reference=True):
        '''处理历史消息中各式各样的markdown格式和json格式'''
        self.logger.info(f"retrieve_content_from_answer data:[{content}]")
        all_contents = ''
        try:
            data = json.loads(content)
            # 遍历列表，提取每个元素的content字段，并进行URL解码
            for item in data:
                content = self.handle_memory_item(item, is_reference)
                if content:
                    all_contents += content
            if len(all_contents) > 20000:
                all_contents = all_contents[:20000]
            format_log(_type="00_log", content=f"检索构造memory,最终返回的answer为[{str(all_contents)}]")
        except Exception as e:
            self.logger.error("加载历史消息时，发生%s异常", str(e), exc_info=True)
        return all_contents

    def handle_memory_item(self, item, is_reference):
        '''
          依次处理历史消息中各式各样的格式，包括MarkDown Data_Visualization AcademicList等
        '''
        content = None
        try:
            if 'MarkDown' == unquote(item['type']) or 'MarkDownTable' == unquote(item['type']):
                content = unquote(item['content'])
                content = (content.replace('<div style="display:flex;flex-wrap:wrap;"><span style="margin-top: 2px; margin-right: 8px">','').replace('</span><font style="background-color:rgba(28, 113, 230, 0.14); padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; margin-right: 8px; border-radius: 6px; margin-bottom: 2px">','').replace('</font><span style="margin-top: 2px">', '').replace('</span></div>', '').replace('Due to copyright issues or other compliance considerations, we have used some of the data provided by Semantic Scholar, which may not be comprehensive, and the copyright of the data still belongs to the author. The following content is for reference only. If you are not satisfied with the results, you can directly go to Semantic Scholar for paper search.', '').replace('由于版权问题或其他合规考虑，我们使用了Semantic Scholar提供的一些数据，这些数据可能不全面，数据的版权仍属于作者，以上内容仅供参考。如果您对结果不满意，可以直接前往专业的学术库进行论文搜索。', '')+ " \n\n ")
            if 'Data_Visualization' == unquote(item['type']) or 'AcademicList' == unquote(item['type']):
                content = json.dumps(item['content'])
            if 'Reference' == unquote(item['type']) and is_reference:
                content = json.dumps(item['content'])
            if 'AcademicList' == unquote(item['type']):
                academic_list_content = item['content']
                number = 0
                format_log(_type="00_log", content=f"检索构造memory,本轮对话为学术检索配置,其content为[{str(academic_list_content)}]")
                content = ''
                for academic_list_content_item in academic_list_content:
                    number = number +1
                    format_log(_type="00_log",content=f"检索构造memory,本轮对话为学术检索配置,当前AcademicList的轮次为[{number}],此处的academic_list_content_item为[{str(academic_list_content_item)}],等待拼接的content为[{str(content)}]")
                    content = content + self.academic_list_content_item_construction(number, academic_list_content_item)
                    format_log(_type="00_log", content=f"检索构造memory,本轮对话为学术检索配置,当前AcademicList的轮次为[{number}],拼接后的content为[{str(content)}]")
            if content and len(content) > 10000:
                content = content[:10000]
            format_log(_type="00_log", content=f"检索构造memory,本轮对话返回的content为[{str(content)}]")
        except Exception as e:
            self.logger.error("加载历史消息时，发生%s异常", str(e), exc_info=True)
            self.logger.error(e)
        return content
    def academic_list_content_item_construction(self, number, academic_list_item):
        '''
          根据AcademicList中content拼接其中的item，拼接其中的每个对象
          {'id': 1, 'tag': 'journal', 'items': [{'text': 'Biostratigraphic%20characteristics%20and%20correction%20of%20the%20boundary%20between%20Miocene%20and%20Oligocene%20sediments%20in%20the%20northern%20Malay%20-%20Tho%20Chu%20basin%3A', 'url': 'https://www.semanticscholar.org/paper/48d612485df073d9e1ba37c99ba366076496c806'}, {'text': 'Stratigraphic%20study%20in%20oil%20and%20gas%20wells%20is%20dependent%20on%20the%20research%20method%20and%20the%20characteristics%20of%20the%20collected%20samples%2C%20such%20as%20sample%20types%20and%20spaces%20between%20samples%2C%20that%20is%20why%20the%20stratigraphic%20boundary%20of%20the%20wells%20may%20fluctuate%20in%20a%20certain%20sedimentary%20range.%20Therefore%2C%20when%20re-evaluating%20the%20hydrocarbon%20potential%20or%20expanding%20the%20petroleum%20exploration%20targets%20of%20an%20area%2C%20we%20need%20to%20study%20additional%20evidence%20and%20geological%20events%20to%20correct%20the%20stratigraphic%20boundary%20of%20the%20well%20an...%20'}, {'text': 'Ho%C3%A0ng%20%C4%90%E1%BA%A3m%20Mai%2C%20Th%E1%BB%8B%20Th%E1%BA%AFm%20Nguy%E1%BB%85n'}, {'text': '%20%E2%80%94%E2%80%94%20%3C%3CPetrovietnam%20Journal%3E%3E'}, {'text': ' —— 2022'}]}
        '''
        academic_list_item_str = ''
        try:
            format_log(_type="00_log",content=f"检索构造memory,本轮对话为学术检索配置,当前AcademicList的轮次为[{number}],其content为[{str(academic_list_item)}]")
            decoded_texts = [unquote(item['text']) for item in academic_list_item['items']]
            academic_list_item_str = str(number) +'  ' + ' '.join(decoded_texts) + " \n\n "
            format_log(_type="00_log",content=f"检索构造memory,本轮对话为学术检索配置,当前AcademicList的轮次为[{number}],解码后拼接得到的academic_list_item_str为[{str(academic_list_item_str)}]")
        except Exception as e:
            self.logger.error(f'学术搜索中,根据AcademicList中content拼接其中的item[{academic_list_item}]出现异常[{str(e)}]')
            self.logger.error(e)
        return academic_list_item_str

