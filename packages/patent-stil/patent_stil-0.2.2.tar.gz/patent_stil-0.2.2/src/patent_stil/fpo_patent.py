import json
import os.path

import pandas as pd
import requests
from bs4 import BeautifulSoup
from .utils import createDirs, downloadFile


class FpoSearchResult:
    def __init__(self, url,label,patent_id, patent_title, patent_abstract,patent_total_num,page):
        self.label=label
        self.patent_id = patent_id
        self.patent_title = patent_title
        self.patent_abstract = patent_abstract
        self.url = url
        self.patent_total_num=patent_total_num
        self.page=page

class FpoPatentInfo:
    def __init__(self,url,patent_id,title,abstract,inventors,application_number,publication_date,filing_date,assignee,primary_class,other_classes,international_classes,field_of_search,pdf_url,view_patent_images,us_patent_references,other_references,primary_examiner,attorney_agent_or_firm,claims,description):
        self.url=url
        self.patent_id=patent_id
        self.title=title
        self.abstract=abstract
        self.inventors=inventors
        self.application_number=application_number
        self.publication_date=publication_date
        self.filing_date=filing_date
        self.assignee=assignee
        self.primary_class=primary_class
        self.other_classes=other_classes
        self.international_classes=international_classes
        self.field_of_search=field_of_search
        self.pdf_url=pdf_url
        self.us_patent_references=us_patent_references
        self.other_references=other_references
        self.primary_examiner=primary_examiner
        self.attorney_agent_or_firm=attorney_agent_or_firm
        self.claims=claims
        self.description=description
        self.view_patent_images=view_patent_images
    def toDataFrame(self):
        x={
            'patent_id':[self.patent_id],
            'title':[self.title],
            'abstract':[self.abstract],
            'inventors':[self.inventors],
            'application_number':[self.application_number],
            'publication_date':[self.publication_date],
            'filing_date':[self.filing_date],
            'assignee':[self.assignee],
            'primary_class':[self.primary_class],
            'other_classes':[self.other_classes],
            'international_classes':[self.international_classes],
            'field_of_search':[self.field_of_search],
            'pdf_url':[self.pdf_url],
            'us_patent_references':[self.us_patent_references],
            'other_references':[self.other_references],
            'primary_examiner':[self.primary_examiner],
            'attorney_agent_or_firm':[self.attorney_agent_or_firm],
            'claims':[self.claims],
        }
        x1={

        }
        for k,v in self.description.items():
            x1[k]=[v]
        return pd.DataFrame(x),pd.DataFrame(x1)
def getFpoSearchResult(query_txt,page=1,sort="relevance",srch="top",patents_us="on",patents_other="off"):
    url=f"https://www.freepatentsonline.com/result.html?p={page}&sort={sort}&srch={srch}&query_txt={query_txt}&submit=&patents_us={patents_us}&patents_other={patents_other}"
    res=requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    if page>200:
        raise Exception("无法浏览超过200页的数据")
    #获取专利总量
    patent_total_num=soup.select_one("#hits")["value"]
    t_table=soup.select_one("#results > div.legacy-container > div > div > table")
    tr_list=t_table.find_all("tr")[1:]
    res=[]
    for tr in tr_list:
        td_list=tr.find_all("td")
        label=int(td_list[0].get_text())
        id = td_list[1].get_text().strip()
        url=f"https://www.freepatentsonline.com"+td_list[2].find("a")["href"]
        title=td_list[2].find("a").get_text().strip()
        abstract=td_list[2].get_text().split("\n")[-1].strip()
        res.append(FpoSearchResult(url,label,id,title,abstract,patent_total_num,page))
    return res

def getFpoPatentInfoByUrl(url):
    res=requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    wrapper=soup.select_one("body > div > div > div.fixed-width.document-details-wrapper")
    div_list=wrapper.find_all("div",{"class":"disp_doc2"})
    field_dict={'title': '', 'abstract': '', 'inventors': '', 'application_number': '', 'publication_date': '', 'filing_date': '',  'assignee': '', 'primary_class': '', 'other_classes': '', 'international_classes': '', 'field_of_search': '', 'view_patent_images': '', 'us_patent_references':'','other_references': '', 'primary_examiner': '', 'attorney_agent_or_firm': '', 'claims': '', 'description': ''}
    for div in div_list:
        div_title=div.find("div",{"class":"disp_elm_title"})
        div_text=div.find("div",{"class":"disp_elm_text"})
        if div_title:
            title = div_title.get_text().replace(" ", "_").lower().replace(",", "").replace(":", "")
            text=div_text.get_text().strip()
            if title not in field_dict.keys():continue
            if title=="inventors":
                text=text.replace("\n",";").replace(" ","")
            if title=="other_classes":
                text=text.replace("\n","").replace(" ","")
            if title=="view_patent_images":
                field_dict["pdf_url"]="https://www.freepatentsonline.com"+div_text.find("a")["href"]
            if title=="other_references":
                text_list=text.split("\n")
                for index,t in enumerate(text_list):
                    text_list[index]=t.strip()
                text="|".join(text_list)
            if title=="us_patent_references":
                tr_list=div_text.find_all("tr")
                res_list=[]
                for tr in tr_list:
                    us_patent_references_dict={}
                    td_list=tr.find_all("td")
                    us_patent_references_dict["patent_id"]=td_list[0].get_text().strip()
                    us_patent_references_dict["title"]=td_list[1].get_text().strip()
                    us_patent_references_dict["date"]=td_list[2].get_text().strip()
                    us_patent_references_dict["author"]=td_list[3].get_text().strip()
                    res_list.append(us_patent_references_dict)
                text=res_list
            if title=="description":
                content_dict={
                }
                headings = soup.find_all("h1")
                for heading in headings:
                    content_list=[]
                    next_element = heading.find_next_sibling()
                    while next_element and next_element.name not in ['h1']:
                        if next_element.name is not None:
                            content_list.append(next_element.get_text().strip())
                        next_element = next_element.find_next_sibling()
                    content_dict[heading.get_text().strip()]="\n".join(content_list)
                text=content_dict
            field_dict[title]=text
    field_dict["url"]=url
    return field_dict

def getFpoPatentInfo(fpo_search_result:FpoSearchResult):
    field_dict=getFpoPatentInfoByUrl(fpo_search_result.url)
    field_dict["patent_id"]=fpo_search_result.patent_id
    return dictToFpoPatentInfo(field_dict)

def downloadFpoPdfByUrl(pdf_url,save_path):
    res=requests.get(pdf_url)
    soup=BeautifulSoup(res.text, "html.parser")
    url_obj=soup.select_one("body > div > div > div:nth-child(3) > center:nth-child(10) > iframe")
    if url_obj:
        return downloadFile(url_obj["src"],save_path)
    else:
        raise Exception(f"无效的地址解析,{pdf_url}")

def dictToFpoPatentInfo(d,patent_id=None):
    if "patent_id" not in d:
        if patent_id is None:
            raise Exception("请指定patent_Id作为唯一标识")
        else:
            d["patent_id"]=patent_id
    return FpoPatentInfo(**d)

def downloadFpoPdf(fpo_patent_info:FpoPatentInfo,save_dir):
    if os.path.basename(save_dir).find(".pdf")!=-1:
        downloadFpoPdfByUrl(fpo_patent_info.pdf_url,save_dir)
    else:
        save_dir=os.path.join(save_dir,f"{fpo_patent_info.patent_id}.pdf")
        downloadFpoPdfByUrl(fpo_patent_info.pdf_url,save_dir)
def autoFpoSpider(query_txt,save_dir="data",save_pdf=True,num_in_search=1,id_is_query=True):
    fpo_search_result_list=getFpoSearchResult(query_txt=query_txt)
    createDirs(save_dir)
    for index,fpo_search_result in enumerate(fpo_search_result_list):
        if index+1>num_in_search:
            break
        fpo_patent_info=getFpoPatentInfo(fpo_search_result)
        base_patent_dir=os.path.join(save_dir,fpo_patent_info.patent_id)
        if id_is_query:
            base_patent_dir = os.path.join(save_dir, query_txt)
        createDirs(base_patent_dir)

        patent_info_dataframe,patent_content_dataframe=fpo_patent_info.toDataFrame()
        patent_info_file=os.path.join(base_patent_dir,f"info.xlsx")
        patent_info_dataframe.to_excel(patent_info_file,index=False)

        patent_content_file = os.path.join(base_patent_dir, f"content.xlsx")
        patent_content_dataframe.to_excel(patent_content_file,index=False)

        with open(os.path.join(base_patent_dir, f"origin_data.json"), "w", encoding="utf-8") as f:
            json.dump(fpo_patent_info.__dict__, f, ensure_ascii=False)
        if save_pdf:
            patent_pdf_file = os.path.join(base_patent_dir, f"patent.pdf")
            downloadFpoPdfByUrl(fpo_patent_info.pdf_url,patent_pdf_file)