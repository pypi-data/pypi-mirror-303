import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 16
project_path = file_path[0:end]
sys.path.append(project_path)



fetch("https://myfavor.eastmoney.com/v4/webouter/as?appkey=e9166c7e9cdfad3aa3fd7d93b757e9b1&cb=jQuery371045745102863162_1727593084438&g=1&sc=116%2402318&_=1727593084478", {
  "headers": {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "cookie": "qgqp_b_id=1e0d79428176ed54bef8434efdc0e8c3; mtp=1; uidal=4253366368931142%e8%82%a1%e5%8f%8b9x56I87727; sid=170711377; vtpst=|; ct=RWJFw3nWsBRloTBCLgO5XX6b48IHj3YiKY0QS2Rn8Vfd14sSHK9v5TAE6wdXndSvskLTqiayWrbw-mHS3wZlLy2Yc0esK7P2WtX_3Pqn_B1ylw0W31ydNOmfMwGdtJEoT8uYVZnOEEKgjGvsZCtXUb5wILUoxwMcjk0Hrjl9meE; ut=FobyicMgeV4IrDnpDeOA2wpy4pz6RNWo-uhd_riT93xOIbOw4OZHlmA5Vsq1An23blEIFsYbBo6zcXjQmAQCxPwQfp4l_z7BCt0O6855lQWHyS4MObxDc9OT11B8PwrZNPxhfY4pQTRMYaXM2aMm0OAXZC-IygpxHk_p83BOWxVYorT-4HoQoLQmix2dcuVG8rd3LKTfjvRJK1zYPIjO_NJe0i-8zEo4B9hmdMkFrGNMHwwG7gmaCZnSDk4s74uv_YstQro7JrrB-5MRdI-xNE9esdGNNM-V; pi=4253366368931142%3Bp4253366368931142%3B%E8%82%A1%E5%8F%8B9x56I87727%3BegTFGhjGzYty9yGOFjlPzZRWVTVOw5PhTyvveXmpLefHG1miuMYvM1XsvT7U3na1uMcMn4s5gPkVCyW%2BLXKU0x0uS%2FqCFE69ubBAbEhaxasiwYbaa9sTVn0HaPC9zWhLNGmoZxykSGh9Xa2aYfqcJeUU4vkPe13ExVrwbSNE44bd2%2B26NIgcGVt1pz7%2F%2FqA8v%2FhkxSn%2F%3BE0adByCvPsoKpsmXX7%2BD2ub2das13Adlj5OiUeTrvF9q6dN54F%2BA0odkH1EZtKjwdUmotY4JmR7x8EHTEoh6PghvOCGUbhm0GcDi2v0qYcBpokFHcQOaz9jIFd0uL1nfkMo96Fb4GWmv9mGrH5iPtjCEKz1bcA%3D%3D; xsb_history=404002%7C%u641C%u7279%u9000%u503A; HAList=ty-0-920019-%u94DC%u51A0%u77FF%u5EFA%2Cty-1-000001-%u4E0A%u8BC1%u6307%u6570%2Cty-0-002296-%u8F89%u714C%u79D1%u6280%2Cty-220-TM-%u5341%u503A%u4E3B%u8FDE%2Cty-0-300133-%u534E%u7B56%u5F71%u89C6%2Cty-0-159546-%u96C6%u6210%u7535%u8DEFETF%2Cty-1-510300-%u6CAA%u6DF1300ETF%2Cty-90-BK0895-%u7EF4%u751F%u7D20%2Cty-1-603777-%u6765%u4F0A%u4EFD%2Cty-90-BK0528-%u8F6C%u503A%u6807%u7684; websitepoptg_api_time=1727593081694; st_si=97341843359922; rskey=XQWMMOHNpaC9BZUFvKzFNYkduYVpvZ0pMQT09ilbyT; st_pvi=26930719093675; st_sp=2024-04-28%2017%3A27%3A05; st_inirUrl=https%3A%2F%2Fcn.bing.com%2F; st_sn=2; st_psi=20240929145804510-113200301712-1483040302; st_asi=20240929145804510-113200301712-1483040302-Web_so_ss-12",
    "Referer": "https://quote.eastmoney.com/zixuan/?from=home",
    "Referrer-Policy": "unsafe-url"
  },
  "body": null,
  "method": "GET"
});