# -*- coding:UTF-8 -*- 
import os,time
import pygal 
import smtplib,email,sys
from email.Header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import mimetypes

from war_redmine_tester import GetData
from war_redmine_designer import GetDesignerData
from war_redmine_developer import GetDeveloperData

i = GetData.setUp()
j = GetDesignerData.setUp()
K = GetDeveloperData.setUp()

#data of tester
Time     = i[0]
LXF      = int(i[1])
YTS      = int(i[2])
SLY      = int(i[3])
WangYang = int(i[4])
LXF_closed      = int(i[5])
YTS_closed      = int(i[6])
SLY_closed      = int(i[7])
WangYang_closed = int(i[8])
WYR      = int(i[9])
WYR_closed      = int(i[10])

#data of designer
XZSH = int(j[1])
YM = int(j[2])
NXY = int(j[3])
YX = int(j[4])
XBW = int(j[5])
LZY = int(j[6])
YCH = int(j[7])
LHR = int(j[8])
QiuH = int(j[9])
XZSH_closed = int(j[10])
YM_closed = int(j[11])
NXY_closed = int(j[12])
YX_closed = int(j[13])
XBW_closed = int(j[14])
LZY_closed = int(j[15])
YCH_closed = int(j[16])
LHR_closed = int(j[17])
QiuH_closed = int(j[18])
DHR = int(j[19])
DHR_closed = int(j[20])
DYY = int(j[21])
DYY_closed = int(j[22])

#data of developer
HCM = int(K[0])
LS = int(K[1])
WW = int(K[2])
QH = int(K[3])
WGJ = int(K[4])
HGF = int(K[5])
WY = int(K[6])
ZY = int(K[7])

#生成图片部分
#tester
bar_chart = pygal.Bar()                                            # Then create a bar graph object
bar_chart.title = "Tester Status"
bar_chart.x_labels = map(str,('LiuXuefeng','SongLiyuan','YuanTianshi','WangYang','WangYanrong'))
bar_chart.add('report_number', [LXF, SLY, YTS, WangYang,WYR])
bar_chart.add('unsolved_number', [(LXF - LXF_closed),(SLY - SLY_closed),(YTS - YTS_closed),(WangYang - WangYang_closed),(WYR - WYR_closed)])
bar_chart.render_to_png('tester.png') 

#designer
bar_chart2 = pygal.Bar()
bar_chart2.title = "designer Status"
bar_chart2.x_labels = map(str,('XueZhisheng','NieXinyu','XueBowei','LiZhiyuan','YuChenghui','LiuHongrui','YangMing','YinXu','QiuHan','DiHaoran','DuYuye'))
bar_chart2.add('report_number', [XZSH,NXY,XBW,LZY,YCH,LHR,YM,YX,QiuH,DHR,DYY])
bar_chart2.add('unsolved_number', [(XZSH - XZSH_closed),(NXY - NXY_closed),(XBW - XBW_closed),(LZY - LZY_closed),(YCH - YCH_closed),\
    (LHR - LHR_closed),(YM - YM_closed),(YX - YX_closed),(QiuH - QiuH_closed),(DHR - DHR_closed),(DYY - DYY_closed)])
bar_chart2.render_to_png('designer.png') 

#developer
bar_chart3 = pygal.Bar()
bar_chart3.title = "developer Status"
bar_chart3.x_labels = map(str,('HuaChangmiao','WangGuojun','HuangGuofang','WeiWei','LiuShuai','QiaoHuan','WangYan'))
bar_chart3.add('unsolved_number', [HCM,WGJ,HGF,WW,LS,QH,WY])
bar_chart3.render_to_png('developer.png') 

#发送邮件模块
def sentmail():
    '''
    #改为html格式后，\n不再合适，故此部分注释掉
    result_name = "War项目人员任务情况统计:" +"\n统计日: " + str(Time) + "\n\n测试人员redmine处理情况如下:\n" + "刘雪峰提交总数量: "+ str(LXF) + "   刘雪峰未处理数量: "+ str(LXF - LXF_closed) \
    + "\n袁天使提交总数量: " + str(YTS) + "   袁天使未处理数量: " + str(YTS - YTS_closed) \
    + "\n宋丽媛提交总数量: " + str(SLY) + "   宋丽媛未处理数量: " + str(SLY - SLY_closed) \
    + "\n\n策划人员redmine处理情况如下:\n" + "薛志盛提交总数量: "+ str(XZSH) + "   薛志盛提的任务未被处理数量: " + str(XZSH - XZSH_closed) \
    + "\n聂新宇提交总数量: " + str(NXY) + "   聂新宇提的任务未被处理数量: " + str(NXY - NXY_closed) \
    + "\n薛博威提交总数量: " + str(XBW) + "   薛博威提的任务未被处理数量: " + str(XBW - XBW_closed) \
    + "\n李志远提交总数量: " + str(LZY) + "   李志远提的任务未被处理数量: " + str(LZY - LZY_closed) \
    + "\n于承慧提交总数量: " + str(YCH) + "   于承慧提的任务未被处理数量: " + str(YCH - YCH_closed) \
    + "\n杨明提交总数量: " + str(YM) + "   杨明提的任务未被处理数量: " + str(YM - YM_closed) \
    + "\n尹旭提交总数量: " + str(YX) + "   尹旭提的任务未被处理数量: " + str(YX - YX_closed) \
    + "\n\n前端人员redmine处理情况如下,任务计划完成日期为统计日:\n" + "华长苗尚未处理的任务: " + str(HCM) \
    + "\n王国军尚未处理的任务: " + str(WGJ) \
    + "\n黄国防尚未处理的任务: " + str(HGF) \
    + "\n魏巍尚未处理的任务: " + str(WW) \
    + "\n刘帅尚未处理的任务: " + str(LS) \
    + "\n乔欢尚未处理的任务: " + str(QH) 
    '''

    result_name = "War项目人员任务情况统计:" +"<br>统计日: " + str(Time) + "<br><br>测试人员redmine处理情况如下:<br>" + "刘雪峰提交总数量: "+ str(LXF) + "   刘雪峰未处理数量: "+ str(LXF - LXF_closed) \
    + "<br>袁天使提交总数量: " + str(YTS) + "   袁天使未处理数量: " + str(YTS - YTS_closed) \
    + "<br>宋丽媛提交总数量: " + str(SLY) + "   宋丽媛未处理数量: " + str(SLY - SLY_closed) \
    + "<br>王洋提交总数量: " + str(WangYang) + "   王洋未处理数量: " + str(WangYang - WangYang_closed) \
    + "<br>王艳荣提交总数量: " + str(WYR) + "   王艳荣未处理数量: " + str(WYR - WYR_closed) \
    + "<br><br>策划人员redmine处理情况如下:<br>" + "薛志盛提交总数量: "+ str(XZSH) + "   薛志盛提的任务未被处理数量: " + str(XZSH - XZSH_closed) \
    + "<br>聂新宇提交总数量: " + str(NXY) + "   聂新宇提的任务未被处理数量: " + str(NXY - NXY_closed) \
    + "<br>薛博威提交总数量: " + str(XBW) + "   薛博威提的任务未被处理数量: " + str(XBW - XBW_closed) \
    + "<br>李志远提交总数量: " + str(LZY) + "   李志远提的任务未被处理数量: " + str(LZY - LZY_closed) \
    + "<br>于承慧提交总数量: " + str(YCH) + "   于承慧提的任务未被处理数量: " + str(YCH - YCH_closed) \
    + "<br>刘弘睿提交总数量: " + str(LHR) + "   刘弘睿提的任务未被处理数量: " + str(LHR - LHR_closed) \
    + "<br>杨明提交总数量: " + str(YM) + "   杨明提的任务未被处理数量: " + str(YM - YM_closed) \
    + "<br>尹旭提交总数量: " + str(YX) + "   尹旭提的任务未被处理数量: " + str(YX - YX_closed) \
    + "<br>邱晗提交总数量: " + str(QiuH) + "   邱晗提的任务未被处理数量: " + str(QiuH - QiuH_closed) \
    + "<br>狄昊然提交总数量: " + str(DHR) + "   狄昊然的任务未被处理数量: " + str(DHR - DHR_closed) \
    + "<br>杜钰叶提交总数量: " + str(DYY) + "   杜钰叶的任务未被处理数量: " + str(DYY - DYY_closed) \
    + "<br><br>前端人员redmine处理情况如下,任务计划完成日期为统计日:<br>" + "华长苗尚未处理的任务: " + str(HCM) \
    + "<br>王国军尚未处理的任务: " + str(WGJ) \
    + "<br>黄国防尚未处理的任务: " + str(HGF) \
    + "<br>魏巍尚未处理的任务: " + str(WW) \
    + "<br>刘帅尚未处理的任务: " + str(LS) \
    + "<br>乔欢尚未处理的任务: " + str(QH) \
    + "<br>王燕尚未处理的任务: " + str(WY)

    #发信邮箱 
    mail_from="zhangjingfeng@playcrab.com"
    #收信邮箱
    #mail_to=["zhangjingfeng@playcrab.com","xuezhisheng@playcrab.com","yangming@playcrab.com","huachangmiao@playcrab.com",\
           #"yuantianshi@playcrab.com","liuxuefeng@playcrab.com","songliyuan@playcrab.com","wangyang@playcrab.com",\
            #"wangyanrong@playcrab.com","srgzyq@playcrab.com"]
    mail_to=["zhangjingfeng@playcrab.com"]
    
    
    subject = '图片html发送邮件测试' 
    msg = MIMEMultipart('alternative') 
    msg['Subject'] = Header(subject,'utf-8')

    fp = open('tester.png','rb') 
    msgImage = MIMEImage(fp.read()) 
    fp.close()
    msgImage.add_header('Content-ID','<image1>') 
    msg.attach(msgImage)
    
    fp = open('designer.png','rb') 
    msgImage = MIMEImage(fp.read()) 
    fp.close()
    msgImage.add_header('Content-ID','<image2>') 
    msg.attach(msgImage)

    fp = open('developer.png','rb') 
    msgImage = MIMEImage(fp.read()) 
    fp.close()
    msgImage.add_header('Content-ID','<image3>') 
    msg.attach(msgImage)
    

    html =  """ 
    <html> 
      <head> </head> 
      <body> 
        <p>图表展示：<br> 
           <br><img src="cid:image1"></br>
           <br><img src="cid:image2"></br> 
           <br><img src="cid:image3"></br> 
        </p> 
      </body> 
    </html> 
    """ 


    htm = MIMEText(result_name + html,'html',_charset='utf-8') 
    msg.attach(htm)

    #定义标题
    msg['Subject']='War项目人员任务情况每日统计'
    smtp=smtplib.SMTP('smtp.office365.com',587)
    smtp.ehlo()
    smtp.starttls()
    #用户名密码
    smtp.login("zhangjingfeng@playcrab.com","billingZJF951413!!")
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()

#调用发邮件模块
sentmail()
