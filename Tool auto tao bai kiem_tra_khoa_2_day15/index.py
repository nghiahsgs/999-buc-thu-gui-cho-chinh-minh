from high_order_framework_requests_python import utils_class
import random

L_en = utils_class.File_Interact('en.txt').read_file_list()
L_vi = utils_class.File_Interact('vi.txt').read_file_list()
L_ex = utils_class.File_Interact('ex.txt').read_file_list()
L_dap_an = []

ndung_html = ''
for index,q in enumerate(L_en):
    # cau hoi 
    ndung_html += '<p><b>%s/ %s</b></p>'%(index,q)
    #goi y
    ndung_html += '<h5>%s</h5>'%(L_ex[index])
    
    true_answer = L_vi[index]
    L_answer = [true_answer]
    L_answer.append(random.choice(L_vi))
    L_answer.append(random.choice(L_vi))

    random.shuffle(L_answer)

    #save lai dap an
    L_dap_an.append(L_answer.index(true_answer))

    #cau tra loi
    ndung_html += '<p>A/ %s</p>'%L_answer[0]
    ndung_html += '<p>B/ %s</p>'%L_answer[1]
    ndung_html += '<p>C/ %s</p>'%L_answer[2]

    ndung_html += '--------\n'

utils_class.File_Interact('kiemtra_html3.html').write_file(ndung_html)

L_dap_an_2 = []
for dap_an in L_dap_an:
    if dap_an ==0:
        dap_an = 'A'
    elif dap_an ==1:
        dap_an = 'B'
    elif dap_an ==2:
        dap_an = 'C'
    elif dap_an ==3:
        dap_an = 'D'
    L_dap_an_2.append(dap_an)
utils_class.File_Interact('dapan.html').write_file_from_list(L_dap_an_2)
