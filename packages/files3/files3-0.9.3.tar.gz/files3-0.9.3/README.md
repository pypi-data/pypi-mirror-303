<h1>Files3 Python Object Management</h1>
<ol>
<li><a href="#en_installation">English Version</li>
<ol>
<li><a href="#en_installation">Intallation</li>
<li><a href="#en_quick_start">Quick Start</li>
<li><a href="#en_advanced">Advanced</li>
<li><a href="#en_notice">Notice</li>
<li><a href="#en_cmd_command">Cmd Command</li>
<li><a href="#en_last">Last</li>
</ol>
<li><a href="#cn_installation">Chinese Version</li>
<ol>
<li><a href="#cn_installation">Intallation</li>
<li><a href="#cn_quick_start">Quick Start</li>
<li><a href="#cn_advanced">Advanced</li>
<li><a href="#cn_cmd_command">Cmd Command</li>
<li><a href="#cn_last">Last</li>
</ol>
</ol>
<a name="en_installation"></a>
<h2>Installation</h2>
<cib-code-block code-lang="python" clipboard-data="pip install files3
"><pre><code class="language-python">pip install files3
</code></pre>
</cib-code-block>
<div style="width: 100%; background-color: rgb(240, 240, 240); border: 1px solid rgb(224, 224, 224); border-radius: 5px; padding: 15px; --darkreader-inline-bgcolor: #f5eee1; --darkreader-inline-border-top: #e5ded1; --darkreader-inline-border-right: #e5ded1; --darkreader-inline-border-bottom: #e5ded1; --darkreader-inline-border-left: #e5ded1;" data-darkreader-inline-bgcolor="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left="">
    <p><b># </b>After installation, you can use the command in cmd: 
    <pre><code class="language-cmd">f3assoc .inst</code></pre>
    to associate the '.inst' file with the 'f3open' program.</p>
</div>
<a name="en_quick_start"></a>
<h2>Quick Start</h2>
<pre><code class="language-python">
from files3 import files
f = files()  # save pyfile in current directory with default suffix '.inst'
&nbsp
## save python object (modify is also like save)
f.set('a', 1)
&nbsp
## check if file exist
f.has('a')  # True
&nbsp
## load python object
print(f.get('a'))  # 1
&nbsp
## delete file
f.delete('a')
</code></pre>
<p>files(dir:str="", type:str=".inst")</p>
<a name="en_advanced"></a>
<h2>Advanced</h2>
<pre><code class="language-python">
from files3 import files
f = files()
&nbsp
## Save
f.a = 1
# f['a'] = 1
&nbsp
## load
print(f.a)  # 1
# print(f['a'])  # 1
&nbsp
## delete
del f.a
# del f['a']
&nbsp
## check if file exist
'a' in f  # False
&nbsp
## sub key
f.c = 1
f['c', 'data'] = [1, 2, 3, 4, 5]  # can only access 'sub key' by getitem && .set. Can only use str in this mode.
print(f.list('c'))
del f['c']  
&nbsp
## Use other key not only str:
# 1. tuple or list
f[('a', 'b')] = [1, 2]
print(f.a, f.b, f['a'], f['b'])  # 1, 2, [1, 2]
&nbsp
# 2. slice
print(f[:])  # [1, 2]
# print(f[...])  # [1, 2]
&nbsp
# 3. function
print(f[lambda x: x == 'a'])  # 1
&nbsp
# 4. re
print(f[re.compile('a')])  # 1
&nbsp
del f[...]
</code></pre>
<pre><code class="language-python">
# hash: get hash of the file
fhash = f.hash('a')
&nbsp
# retype: adjust the ftype of exists files
f.retytpe('.newtype', 'a', 'b', ...)  # f.retype('.newtype')  # all files
&nbsp
# relink: manual adjust the scp(Source Code Path) of exists files 
f.retytpe('C:/mycode/code.py', 'a', 'b', ...)  # f.retype('C:/mycode/code.py')  # all files
</code></pre>
<a name="en_notice"></a>
<h2>Notice</h2>
<p>There are some special case that you can't save:</p>
<ol>
    <li>f3bool object and files object (alias Files, F3Shell)</li><li>Actively refuse to serialize objects (such objects will actively throw errors when attempting to serialize)</li><li>cases not supported by pickle (such as module, lambda, local function/class (that is nested inside other functions and classes))</li>
</ol>
<a name="en_cmd_command"></a>
<h2>Cmd Command</h2>
<pre><code>
f3 [name] [type] -d [dir]  # open a files3 object
f3open [fpath]  # open a files3 object
f3assoc [type]  # associate the '.type' file with the 'f3open' program
</code></pre>
<a name="en_last"></a>
<h2>Last</h2>
<p>It's really convinent but, because pickle is not safe, so mayn't use it to load the file you don't trust. However, if you do not care about it like me, you can use it to bring you a good programming experience.</p>

<a name="cn_installation"></a>
<h2>安装files3</h2>
<cib-code-block code-lang="python" clipboard-data="pip install files3
"><pre><code class="language-python">pip install files3
</code></pre>
</cib-code-block>
<div style="width: 100%; background-color: rgb(240, 240, 240); border: 1px solid rgb(224, 224, 224); border-radius: 5px; padding: 15px; --darkreader-inline-bgcolor: #f5eee1; --darkreader-inline-border-top: #e5ded1; --darkreader-inline-border-right: #e5ded1; --darkreader-inline-border-bottom: #e5ded1; --darkreader-inline-border-left: #e5ded1;" data-darkreader-inline-bgcolor="" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left="">
    <p><b># </b>安装后，可以在cmd中使用命令：
    <pre><code class="language-cmd">f3assoc .inst</code></pre>
    将'.inst'文件关联到'f3open'程序。</p>
</div>
<a name="cn_quick_start"></a>
<h2>快速开始</h2>
<pre><code class="language-python">
from files3 import files
f = files()  # 保存py文件在当前目录，后缀为'.inst'
&nbsp
## 保存python对象（修改也是这样）
f.set('a', 1)
&nbsp
## 检查文件是否存在
f.has('a')  # True
&nbsp
## 加载python对象
print(f.get('a'))  # 1
&nbsp
## 删除文件
f.delete('a')
</code></pre>
<p>files(dir:str="", type:str=".inst")</p>
<a name="cn_advanced"></a>
<h2>高级用法</h2>
<pre><code class="language-python">
from files3 import files
f = files()
&nbsp
## 保存
f.a = 1
# f['a'] = 1
&nbsp
## 加载
print(f.a)  # 1
# print(f['a'])  # 1
&nbsp
## 删除
del f.a
# del f['a']
&nbsp
## 检查文件是否存在
'a' in f  # False
&nbsp
## 使用子键
f.c = 1
f['c', 'data'] = [1, 2, 3, 4, 5]  # 子键模式只能使用getitem和.set这两种方式。子键模式只能使用str进行索引
print(f.list('c'))
del f['c']  
&nbsp
## 使用其他键不仅仅是str：
# 1. tuple or list
f[('a', 'b')] = [1, 2]
print(f.a, f.b, f['a'], f['b'])  # 1, 2, [1, 2]
&nbsp
# 2. slice
print(f[:])  # [1, 2]
# print(f[...])  # [1, 2]
&nbsp
# 3. function
print(f[lambda x: x == 'a'])  # 1
&nbsp
# 4. re
print(f[re.compile('a')])  # 1
&nbsp
del f[...]
</code></pre>
<pre><code class="language-python">
# hash：获取目标的文件指纹
fhash = f.hash('a')
&nbsp
# retype: 调整已有文件的后缀
f.retytpe('.newtype', 'a', 'b', ...)  # f.retype('.newtype')  # 全部文件
&nbsp
# relink: 手动调整已有文件的源代码后位置
f.retytpe('C:/mycode/code.py', 'a', 'b', ...)  # f.retype('C:/mycode/code.py')  # 全部文件
</code></pre>
<a name="cn_notice"></a>
<h2>注意</h2>
<p>有一些特殊情况不能保存：</p>
<ol>
<li>f3bool对象和files对象(别名Files, F3Shell)</li>
<li>主动拒绝序列化的对象(例如此类对象在试图序列化时会主动抛出error)</li>
<li>pickle不支持的情况(例如 module，lambda，local function/class (那种嵌套在其他函数和class内部的))</li>
</ol>
<a name="cn_cmd_command"></a>
<h2>Cmd命令</h2>
<pre><code>
f3 [name] [type] -d [dir]  # 打开一个files3对象
f3open [fpath]  # 打开一个files3对象
f3assoc [type]  # 将'.type'文件关联到'f3open'程序
</code></pre>
<a name="cn_last"></a>
<h2>最后</h2>
<p>这确实很方便，但是由于pickle不安全，因此可能不要使用它来加载您不信任的文件。 但是，如果您不像我一样不怎么关心它，那么可以使用它为您带来良好的编程体验。</p>

