from librarys.materials_management import Material
class TestMaterial:
    def test_001(self):
        self.test_001 = Material(self.driver)
        self.test_001.add_raw_material(materialType='材料分类930',materialName='材料930',materialSpecification='12*129999*12',unit='箱',singleWeight='3',unitPrice='15')