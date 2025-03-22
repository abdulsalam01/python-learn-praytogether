# library/utils/helper -> memudahkan proses yang ingin kita capai
from staticmap import StaticMap, Line

# link library: https://github.com/komoot/staticmap
m = StaticMap(300, 400, 10)
m.add_line(Line(((13.4, 52.5), (2.3, 48.9)), 'blue', 3))
image = m.render()
image.save('./map.png')

# keyword untuk check versi pip
# pip / pip3 --version

# keyword untuk install package
# pip / pip3 install <nama-package>

# bundle package apa aja sih yang kita punya
# pip / pip3 freeze > requirements.txt

# install package yang terdaftar (recursively)
# pip / pip3 install -r requirements.txt