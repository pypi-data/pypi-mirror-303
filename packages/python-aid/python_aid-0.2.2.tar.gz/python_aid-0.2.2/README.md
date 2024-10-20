# python-aid
`python-aid`は、Misskeyで利用可能なIDアルゴリズムを実装して利用できるようにしたPythonライブラリです。

## aid/aidxとは？
Misskeyで利用されているID生成アルゴリズムです。ミリ秒単位の精度があります。

## Example
### aid
```python
from python_aid import aid

generated = aid.genAid()
print("aid: " + generated)

print("time: " + aid.parseAid(generated).strftime('%Y-%m-%d %H:%M:%S.%f'))
```
#### With timestamp
```python
from python_aid import aid

generated = aid.genAid(timestamp=1718546963) # 1718546963 = 2024/06/16 23:09:23 (JST)
print("aid: " + generated)

print("time: " + aidx.parseAid(generated).strftime('%Y-%m-%d %H:%M:%S.%f'))
```
### aidx
```python
from python_aid import aidx

generated = aidx.genAidx()
print("aidx: " + generated)

print("time: " + aidx.parseAidx(generated).strftime('%Y-%m-%d %H:%M:%S.%f'))
```
#### With timestamp
```python
from python_aid import aidx

generated = aidx.genAidx(timestamp=1718546963) # 1718546963 = 2024/06/16 23:09:23 (JST)
print("aidx: " + generated)

print("time: " + aidx.parseAidx(generated).strftime('%Y-%m-%d %H:%M:%S.%f'))
```
## 試す
[python-aid sandbox](https://codepiece.pages.dev/?state=N4Igxg9gJgpiBcIBmAnCBbABABwJ4BcALCAOwH0BDASykyvWwhX02qgA8AdE7gcxhIwUFfDFoBeVjXYA6fiQCC0gBQBKbthRUS%2BZZxBt28TPswBqTPKEix6niU3bd%2B%2FPRjHTFwzOwUUAZxglDmUrYVEoVRl%2FfBQkV3QYZQByAFIATQBaVPRs2lSACXhUgFligGUZVKRk1VUQABoQXzAAawp%2BfwQAbWaCYhJMthAAXSb8P358BBAYqAgAV2mm%2BYB3EgAbCAooLvhukYBfIA%3D%3D)
