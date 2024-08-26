from django.shortcuts import render

# Create your views here.
# invoices/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm
import pandas as pd
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import pandas as pd
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from .models import Employee
from datetime import datetime

def create_invoice_excel(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    data = {
        'Name': [employee.name],
        'Position': [employee.position],
        'Total Regular Hours': [employee.total_hours],  # Assuming total_hours includes regular hours
        'Total Overtime Hours': [employee.total_overtime_hours],
        'Total Regular Pay': [employee.total_regular_pay],
        'Total Overtime Pay': [employee.total_overtime_pay],
        'Total Pay': [employee.total_pay],
    }
    df = pd.DataFrame(data)
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Invoice', index=False)
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from .models import Employee
from datetime import datetime

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from .models import Employee
from datetime import datetime

def create_invoice_pdf(request, employee_id):
    # Fetch employee details
    employee = get_object_or_404(Employee, id=employee_id)

    # Create a PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{employee.name}_invoice.pdf"'

    # Create a PDF document
    doc = SimpleDocTemplate(response, pagesize=letter)

    # Define styles
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    title_style.fontSize = 18
    title_style.alignment = 1  # Centered
    title_style.textColor = colors.HexColor("#004080")  # Dark blue color

    normal_style = styles['Normal']
    normal_style.fontSize = 12

    # Company Information
    company_info = [
        ["STAFFING SOLUTION R US LLC", ""],
        ["8735 DUNWOODY PLACE #4618", ""],
        ["ATLANTA, GA 30350", ""]
    ]

    # Content list to hold the elements of the document
    content = []

    # Company Information Table
    company_table = Table(company_info, colWidths=[4 * inch, 2 * inch])
    company_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#004080")),  # Dark blue header
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # White text
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # White background
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),  # Black text
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
    ]))
    content.append(company_table)
    content.append(Spacer(1, 0.5 * inch))  # Add space below the company info

    # Title
    content.append(Paragraph("Invoice Receipt", title_style))
    content.append(Spacer(1, 0.25 * inch))  # Add space below the title

    # Date and Employee Information
    content.append(Paragraph(f"Date: {datetime.now().strftime('%Y-%m-%d')}", normal_style))
    content.append(Paragraph(f"Employee: {employee.name}", normal_style))
    content.append(Paragraph(f"Position: {employee.position}", normal_style))
    content.append(Spacer(1, 0.5 * inch))  # Add space below the employee info

    # Table Data
    table_data = [
        ["Description", "Amount"],
        ["Total Regular Hours", f"{employee.total_hours:.2f}"],
        ["Rate per Hour", f"${employee.regular_hour_rate:.2f}"],
        ["Total Regular Pay", f"${employee.total_regular_pay:.2f}"],
        ["Total Overtime Hours", f"{employee.total_overtime_hours:.2f}"],
        ["Rate per Hour", f"${employee.overtime_hour_rate:.2f}"],
        ["Total Overtime Pay", f"${employee.total_overtime_pay:.2f}"],
        ["Total Pay", f"${employee.total_pay:.2f}"]
    ]

    # Create a table
    table = Table(table_data, colWidths=[4 * inch, 2 * inch])

    # Style the table
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#CCE5FF")),  # Light blue header
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor("#004080")),  # Dark blue text
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),  # Font size for headers
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#E6F2FF")),  # Very light blue rows
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#004080")),  # Dark blue gridlines
    ]))

    content.append(table)
    content.append(Spacer(1, 0.5 * inch))  # Add space below the table

    # Add a footer
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=10,
        alignment=1,  # Centered
        textColor=colors.HexColor("#004080"),  # Dark blue color
    )
    content.append(Paragraph("Thank you for your hard work!", footer_style))

    # Build the PDF
    doc.build(content)

    return response


# invoices/views.py
from django.shortcuts import render, redirect
from .forms import EmployeeForm


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect to the list of employees after saving
    else:
        form = EmployeeForm()

    return render(request, 'add_employee.html', {'form': form})

from django.urls import reverse

def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect(reverse('employee_list'))
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update_employee.html', {'form': form})

# View to delete an employee
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect(reverse('employee_list'))
    return render(request, 'confirm_delete.html', {'employee': employee})
