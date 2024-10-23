from deep_translator import GoogleTranslator


class RussianToChineseTranslator:
    def __init__(self):
        self.translator = GoogleTranslator(resource='ru', target='zh-CN')

    def translate(self, text):
        try:
            result = self.translator.translate(text, src='ru', dest='zh-cn')
            return result
        except Exception as e:
            print('trans error#', e)
            return 'trans error'

    def long_text_trans(self, text, max_length=4000):
        text_list = [text[i:i + max_length] for i in range(0, len(text), max_length)]
        res_text = ''
        for t in text_list:
            res_text += self.translate(t)
        return res_text