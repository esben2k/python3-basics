#class multi import

#import an entire module
import class_import_multiple_modular as cimm

my_bw_ereader = cimm.Ereader('amazon','paperweight','adjustable','several months of battery life', '300dpi')
print (my_bw_ereader.get_ereader_name())

my_color_ereader = cimm.KindleFire('amazon','kindle fire','color screen','12 hours of battery','1280*800 resolution')
print(my_color_ereader.get_ereader_name())


#import all classes from module
#from class_import_multiple_modular import *

"""
#import specific classes from a module
from class_import_multiple_modular import Ereader, KindleFire

my_bw_ereader = Ereader('amazon','paperweight','adjustable','several months of battery life', '300dpi')
print (my_bw_ereader.get_ereader_name())

my_color_ereader = KindleFire('amazon','kindle fire','color screen','12 hours of battery','1280*800 resolution')
print(my_color_ereader.get_ereader_name())

"""