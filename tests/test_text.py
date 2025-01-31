from . import *

wastemoney=False
class TestText(TestGeneric):
    """Testing the text method of FuncNotify
    """    
    # Tests if text alerts are working, set waste money to true if u want to test, costs money
    def test_Method(self, *args, **kwargs):
        if wastemoney:
            time_func(self.wait_test, use_env=True, update_env=True, NotifyMethod="Text", *args, **kwargs)()
            self.confirm_method(TextMethod)
            self.confirm_cred()
    def test_Decorator(self, *args, **kwargs):
        if wastemoney:
            time_Text(wait_test, use_env=True, *args, **kwargs)()
            self.confirm_method(TextMethod)
            self.confirm_cred()
    
    def test_Stress(self):
        if wastemoney:
            self.stressMethod(self.test_Method, time_=2, count=5)
    