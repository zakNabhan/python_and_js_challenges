 
test = """
          plant,
                    ml,
                    scheduled_batches,
                    scheduled_date,
                    group_cd,
                    ser,
                    rev,
                    sap_order_num,
                    server_first_seen_utc,
                    server_first_consumption_utc,
                    server_last_seen_utc
            
"""
newlist = test.split()
for x in newlist:
  
    #d = x.replace(",", ")")
    without = x.replace(",", " ")
    #print(f"%({without})s,".replace(" ", ""))
    
    #print(f'{without}'.replace(" ", "") +" "+ "=" + " "+f"%({without})s,".replace(" ", ""))
   

    print(f'"{without}"'.replace(" ", "") + ":" + " "+f"payload['{without}'],".replace(" ", ""))

