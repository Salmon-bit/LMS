from docxtpl import DocxTemplate

doc = DocxTemplate("decree_template.docx")
i = input().split("/")
dc = {"ruler": i[0], "item": i[1], "palace": i[2]}
doc.render(dc)
doc.save("order.docx")