with open('./datos/filecomp1_html.txt', 'r') as file1:
    with open('./datos/filecomp2_html.txt', 'r') as file2:
        difference = set(file1).difference(file2)

with open('./datos/diffcomp_html.txt', 'w') as file_out:
    for line in difference:
        file_out.write(line)
