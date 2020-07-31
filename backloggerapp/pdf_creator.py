import os
from typing import Optional
from django.db.models.query import QuerySet
import fpdf
from backlogger.settings import STATICFILES_DIRS

def update_or_create_pdf(owner: str,project: Optional[QuerySet],entries: QuerySet = None ) -> None:
    """Creates the first page and a plan subpage
       or updates entries if they already exist   
    
    """
    
    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_author("BackLogger")
    pdf.set_font("Arial",size=20,style="B")
    pdf.multi_cell(200,50,align="C",txt=f"{owner.capitalize()}'s project")
    pdf.line(10, 50, 200, 50)
    pdf.set_font("Arial",size=17,style="I")
    pdf.multi_cell(200,6,align="C",txt="Plan")
    pdf.line(95,70,125,70)
    pdf.ln(15)
    for ent in project:
        pdf.set_font("Arial",size=17)
        pdf.write(10,ent.project_plan)
    
    if entries is not None:
        pdf.add_page()
        pdf.set_font("Arial",size=17,style="I")
        pdf.multi_cell(200,10,txt="Entries",align="C")
        pdf.line(95,20,125,20)
        pdf.set_font("Arial",size=17)
        for num,ent in enumerate(list(entries)):
            pdf.ln(15)
            pdf.write(10,f"Entry number : {num+1}")
            pdf.ln(15)
            pdf.write(10,ent.name_of_the_entry)
            pdf.ln(10)
            pdf.write(10,ent.description)
        pdf.output(name=os.path.join(STATICFILES_DIRS[2][1],f"{owner}_{[x.name for x in project][0]}.pdf"))  
    else:
        pdf.output(name=os.path.join(STATICFILES_DIRS[2][1],f"{owner}_{[x.name for x in project][0]}.pdf"))