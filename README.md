# pycb
## PYCB, um Contador de 'Bactéria' em Python
Este "programa" foi desenvolvido em 7.5.2019 para atender as obrigações da disciplina *Processamento de Imagens Médicas* da USP-RP (FFCLRP). Ele conta colônias da bactéria Staphilococcus aureus em placas de ágar. O processo está documentado no código (*pycb.py*).

## Estágios do processo

.                                               |  .
:----------------------------------------------:|:------------------------------------------------:
<img src="/estagios/0-orig.jpg" width="240">    |  <img src="/estagios/1-mask.jpg" width="240">
<img src="/estagios/2-gray.jpg" width="240">    |  <img src="/estagios/3-blur.jpg" width="240">
<img src="/estagios/4-edge.jpg" width="240">    |  <img src="/estagios/5-dilate.jpg" width="240">
<img src="/estagios/6-erode.jpg" width="240">    |  <img src="/estagios/7-contours.jpg" width="240">

## Comparações

Original                                        |  Processada
:----------------------------------------------:|:------------------------------------------------:
<img src="/comparacoes/q120404-01.jpg" width="480">    |  <img src="/comparacoes/q120404-01.jpg-out.jpg" width="480">

Para mais comparações, acesse o diretório (comparacoes)[https://github.com/jcbrtl/pycb/tree/master/comparacoes].


## Agradecimentos
Amostras das placas obtidas em: http://opencfu.sourceforge.net/samples.php

## Dependências
> $ pip3 install numpy argparse imutils opencv-python

## Uso
> $ python3 pycb.py -i [arquivo_imagem]

## Licença
```
Copyright 2019 J. Cesar Bertelli <jcbrtl-@-usp-.-br>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
````

## Links úteis
- https://docs.opencv.org/2.4/index.html
- https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html#py-table-of-content-imgproc
- https://en.wikipedia.org/wiki/Green%27s_theorem#Area_calculation
- https://en.wikipedia.org/wiki/Shoelace_formula
- https://www.learnopencv.com/convex-hull-using-opencv-in-python-and-c/

.
