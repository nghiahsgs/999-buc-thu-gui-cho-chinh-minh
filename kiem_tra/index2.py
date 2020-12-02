from high_order_framework_requests_python import utils_class
import random

L_en = utils_class.File_Interact('en.txt').read_file_list()
L_vi = utils_class.File_Interact('vi.txt').read_file_list()

ndung_html = ''
for index,q in enumerate(L_en):
    ndung_html += '<p><b>%s/ %s</b></p>'%(index,q)
    
    L_answer = [L_vi[index]]
    L_answer.append(random.choice(L_vi))
    L_answer.append(random.choice(L_vi))

    random.shuffle(L_answer)

    ndung_html += '<p>A/ %s</p>'%L_answer[0]
    ndung_html += '<p>B/ %s</p>'%L_answer[1]
    ndung_html += '<p>C/ %s</p>'%L_answer[2]

    ndung_html += '--------\n'

utils_class.File_Interact('kiemtra_html2.html').write_file(ndung_html)