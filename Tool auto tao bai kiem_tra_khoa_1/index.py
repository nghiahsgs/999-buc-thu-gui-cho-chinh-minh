from high_order_framework_requests_python import utils_class

L = utils_class.File_Interact('input.txt').read_file_list()

L = list(dict.fromkeys(L))

utils_class.File_Interact('output.txt').write_file_from_list(L)