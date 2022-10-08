from selenium.webdriver.common.by import By
class Material:
    def __init__(self,driver):
        self.driver = driver

    def add_raw_material(self,materialType,materialName,materialSpecification,unit,singleWeight,unitPrice):
        """新增原材料"""
        self.driver.find_element(By.XPATH, '//span[text()="材料管理"]').click() #点击材料管理
        self.driver.find_element(By.XPATH, '//span[text()="新增"]').click() #点击新增
        self.driver.find_element(By.XPATH, '/html/body/div[6]/div/section/form/div[1]/div/div/div[2]/div/div').click() #点击点击材料图片
        #上传材料图片
        import pywinauto
        from pywinauto.keyboard import send_keys
        # 使用pywinauto来选择文件
        app = pywinauto.Desktop()
        # 选择文件上传的窗口
        dlg = app["打开"]
        # 选择文件地址输入框，点击激活
        dlg["Toolbar3"].click()
        # 键盘输入上传文件的路径
        send_keys("C:\\Users\\Administrator\\Desktop")
        # 键盘输入回车，打开该路径
        send_keys("{VK_RETURN}")
        # 选中文件名输入框，输入文件名
        dlg["文件名(&N):Edit"].type_keys("1.png")
        # 点击打开
        dlg["打开(&O)"].click()
        self.driver.find_element(By.XPATH, '//label[text()="材料分类"]/..//input').send_keys(materialType)#选择材料分类
        self.driver.find_element(By.XPATH, '//label[text()="材料名称"]/..//input').send_keys(materialName)#选择材料名称
        self.driver.find_element(By.XPATH, '//label[text()="材料规格(mm)"]/..//input').send_keys(materialSpecification)#输入材料规格
        self.driver.find_element(By.XPATH, '//label[text()="单位"]/..//input').send_keys(unit)#输入单位
        self.driver.find_element(By.XPATH, '//label[text()="单个重量(KG)"]/..//input').send_keys(singleWeight)#输入单个重量
        self.driver.find_element(By.XPATH, '//label[text()="单价(元)"]/..//input').send_keys(unitPrice)#输入单价
        self.driver.find_element(By.XPATH, '/html/body/div[6]/h2/span[1]').send_keys(unitPrice)#点击空白
        self.driver.find_element(By.XPATH, '//div[@class="xm-footer"]//span').click()#点击确定
















