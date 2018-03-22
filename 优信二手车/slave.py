import requests
from lxml import etree
import mongo_or
import master
class Slave_Spisder():
    def parse_detail_data(self,html):
        data=dict()
        model_name = html.xpath('//div[@class="cd_m_info cd_m_info_zjf"]/div[2]/div[1]/span/text()')[0].strip()
        data["车型名字"] = model_name
        car_age =html.xpath('//ul[@class="cd_m_info_desc"]/li[1]/span/text()')
        data["车龄"] = car_age
        car_mileage = html.xpath('//ul[@class="cd_m_info_desc"]/li[2]/a/text()')[0].strip()
        data["排量"] = car_mileage
        emission_stand = html.xpath('//ul[@class="cd_m_info_desc"]/li[3]/span[1]/text()')
        data["排放标准"] = emission_stand
        displa = html.xpath('//ul[@class="cd_m_info_desc"]/li[4]/span[1]/text()')
        data["里程"] =  displa
        raw_price = html.xpath('//p[@class="cd_m_info_price"]/span[2]/span/span/span/b/text()')
        getcar_time = html.xpath('//ul[@class="cd_m_info_desc"]/li[5]/span[1]/text()')
        data["车龄"] = getcar_time
        yearly_check_due = html.xpath('//div[@class="cd_m_i_pz"]/dl[1]/dd[4]/span[2]/text()')
        data["年检到期"] = yearly_check_due
        insurance_due = html.xpath('//div[@class="cd_m_i_pz"]/dl[1]/dd[5]/span[2]/text()')
        data["保险到期"] = insurance_due
        mainten_situ = html.xpath('//div[@class="cd_m_i_pz"]/dl[1]/dd[6]/span[2]/text()')
        data["保养情况"] = mainten_situ
        car_made = html.xpath('//div[@class="cd_m_i_pz"]/dl[2]/dd[1]/span[2]/a/text()')[0].strip()
        data["制造商"] = car_made
        car_mod = html.xpath('//div[@class="cd_m_i_pz"]/dl[2]/dd[2]/span[2]/a/text()')[0].strip()
        data["车型"] = car_mod
        color = html.xpath('//div[@class="cd_m_i_pz"]/dl[2]/dd[3]/span[2]/a/text()')[0].strip()
        data["颜色"] = color
        struct =html.xpath('//div[@class="cd_m_i_pz"]/dl[2]/dd[4]/span[2]/a/text()')[0].strip()
        data["车身结构"] = struct
        engin = html.xpath('//div[@class="cd_m_i_pz"]/dl[3]/dd[1]/span[2]/text()')
        data["发动机"] = engin
        transmiss = html.xpath('//div[@class="cd_m_i_pz"]/dl[3]/dd[2]/span[2]/a/text()')[0].strip()
        data["变速箱"] = transmiss
        fuel_mode = html.xpath('//div[@class="cd_m_i_pz"]/dl[3]/dd[4]/span[2]/text()')
        data["燃油类型"] = fuel_mode
        drive_mode = html.xpath('//div[@class="cd_m_i_pz"]/dl[3]/dd[5]/span[2]/text()')
        data["驱动形式"] = drive_mode
        fuel_consum = html.xpath('//div[@class="cd_m_i_pz"]/dl[3]/dd[6]/span[2]/text()')
        data["油耗"] = fuel_consum
        items = html.xpath('/html/body/div[2]/div[13]/div/div[4]/div[1]/dl[1]/dd[1]/span[2]')
        print(items)
    def get_pro_data(self,html):
        pass


        # return data
        #以下爬取的是车辆的质量检测报告项目



if __name__ == '__main__':
    pass






