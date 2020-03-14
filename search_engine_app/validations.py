
"""This class is valideate whether user input is English or not
@Author: Adarsh Koppa Manjunath
@Input
    topic(str)
@Output
    Boolean""""
class validation:
    def isEnglish(self,topic):
        try:
            topic.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            return False
        else:
            return True
