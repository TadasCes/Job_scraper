import re
from bs4 import BeautifulSoup
import requests
from time import sleep
from random import randint
from job import Job
from generate_report import generate_report

# from os import system
# system("clear")

page_section = ""
page_count = 0
jobs = []

URL = "https://www.cvbankas.lt/?miestas=Vilnius&padalinys%5B0%5D=76&page=0"
page = requests.get(URL)
first_page = BeautifulSoup(page.content, "html.parser")
page_section = first_page.find("ul", class_="pages_ul_inner")
page_count = len(page_section.find_all("a")) + 1


def dev_printJobs(jobs):
    for job in jobs:
        print(job.company)
        print(job.position)
        print(job.salary)
        print(job.link)
        print()


def dev_print_job(job):
    print(job.company)
    print(job.position)
    print(job.salary)
    print(job.link)
    print()


def calculateNeto(bruto):
    bruto = int(bruto)
    neto = 0
    NPD = 400
    Pajamu_mokestis = 0.20
    Sveikatos_draudimas = 0.0698
    Pensiju_soc_draudimas = 0.1252
    if bruto > 2864:
        NPD = 0
    elif bruto > 642:
        NPD = NPD - 0.18 * (bruto - 642)

    PD = bruto - NPD
    neto = bruto - ((PD*Pajamu_mokestis)
                    + (bruto*Sveikatos_draudimas)
                    + (bruto*Pensiju_soc_draudimas))
    print(neto)
    return neto


def addNewJob(job):
    job_company = job.find("span", class_="dib mt5")
    job_position = job.find("h3", class_="list_h3")
    job_salary_amount = job.find("span", class_="salary_amount")
    job_salary_period = job.find("span", class_="salary_period")
    job_salary_calculation = job.find(
        "span", class_="salary_calculation")

    if None == job_salary_amount:
        job_salary = "Nenurodyta"
    else:
        job_salary = job_salary_amount.text + " " + \
            job_salary_period.text + " - " + job_salary_calculation.text

    link = job.find('a')['href']

    # print(job_company.text)
    # print(job_position.text)
    # print(job_salary)
    # print(link)
    # print()

    jobs.append(Job(
        job_company.text,
        job_position.text,
        job_salary,
        link
    ))


def get_all_viable_jobs(search_term):
    global jobs
    jobs = []
    print(len(jobs))
    page_number = 5
    while page_number <= page_count:
        # print("Page number: " + str(page_number))
        new_page = requests.get(
            "https://www.cvbankas.lt/?miestas=Vilnius&padalinys%5B0%5D=76&page=" + str(page_number))
        # sleep(randint(0, 1))

        new_info = BeautifulSoup(new_page.content, "html.parser")
        job_section = new_info.find(id="js_id_id_job_ad_list")

        job_list = job_section.find_all('article', class_="list_article")

        for job in job_list:
            job_name = job.find("h3").text.lower()
            if search_term in job_name:
                addNewJob(job)

        page_number += 1
    return jobs


# getAllViableJobs()
# generate_report(jobs)
