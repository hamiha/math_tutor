'''
data = {
    "detection_list": [],
    "detection_map": {
        "contains_chart": 0,
        "contains_diagram": 0,
        "contains_geometry": 0,
        "contains_graph": 0,
        "contains_table": 0,
        "is_inverted": 0,
        "is_not_math": 0,
        "is_printed": 0
    },
    "error": "",
    "latex": "\\lim _ { x \\rightarrow 3} ( \\frac { x ^ { 2} + 9} { x - 3} )",
    "latex_confidence": 0.86757309488734,
    "position": {
        "height": 273,
        "top_left_x": 57,
        "top_left_y": 14,
        "width": 605
    }
}
print(data['latex'])
'''
#!/usr/bin/env python
import sys
import base64
import requests
import json
import re
'''

file_path = "integral.jpg"
image_uri = "data:image/jpeg;base64," + base64.b64encode(open(file_path, "rb").read())
# (python3) image_uri = "data:image/jpg;base64," + base64.b64encode(open(file_path, "rb").read()).decode()
r = requests.post("https://api.mathpix.com/v3/latex",
    data=json.dumps({'url': image_uri, 'callback': {'post': 'http://requestb.in/10z3g561', 'reply': file_path}}),
    headers={"app_id": "devminhhai_gmail_com", "app_key": "ceb7df5d2d13f08405f4",
        "Content-type": "application/json"})
print(r.text)
'''
save = []
string = r"\left. \begin{array} { l } { x ^ { 2 } + 2 x = 0 } \\ { x \cdot ( x + 2 ) = 0 } \\ { x = 0 } \\ { x = - 2 } \end{array} \right."
print(string)
string1 = string.strip()
print(string1)
string2 = string.split(r'\\')
print(string2)
for s in string2:
    s1 = s.split(' ')
    #print(s1)
    s1 = [s2 for s2 in s1 if s2 not in [r"\left.",r"\begin{array}",r"\end{array}",r"\right."]]
    temp = ' '.join(s1)
    temp = temp.replace(' ', '')
    if temp[:3] == "{l}":
        temp = temp[3:]
    print(temp)
    temp1 = temp.replace("\\\\","")
    print(temp1)
    save.append(temp1)
print(save)
for item in save:
    print(save)
    temp1 = item.replace("\\\\","|")
    print(temp1)
    match =  re.search(r"\\", temp1)
    if match:
        print("match", match)
        print(match.span())
        temp1 = temp1[:match.span()[0]]+temp1[match.span()[1]:]
        print(temp1)
        tmp = temp1
save.append(tmp)
print(save)

string = r"\int _{ 1 } ^ { 3 } \int_ { 0 } ^ { 2 } \operatorname { ln } ( x + y ) d x d y"
