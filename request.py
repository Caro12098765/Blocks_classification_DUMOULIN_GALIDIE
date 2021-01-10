import requests
res = requests.post('http://localhost:5000/api_Block_Classification', 
                    json={"height":int(5),
                          "length":int(7),
                          "area":int(35),
                          "eccen":float(1.4),
                          "p_black":float(0.4),
                          "p_and":float(0.657),
                          "mean_tr":float(2.33),
                          "blackpix":int(14),
                          "blackand":int(23),
                          "wb_trans":int(6)})
if res.ok:
    print(res.json())
