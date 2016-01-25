# Decblog
Decblog是一个简单的，基于Django框架的个人博客系统，[Demo参考站点](http://litp.applinzi.com/)。
规划思想主要受到[MayBlog](https://github.com/flyhigher139/mayblog)的影响（名字就是因为代码是从2015年12月开始写的，所以叫作**Dec**ember**Blog**，跟MayBlog学的）。

## 特征
一些特征有：
* 使用markdown保存博客文章，图片等媒体资源放在CDN上
* 使用Python的fenced-code-blocks进行代码高亮
* 博客文章链接使用静态URL
* 使用[多说评论](http://www.duoshuo.com)系统
* 使用Django自带的Classed Based View
* 后台管理使用Django的Admin
* CSS使用simple grid实现响应式设计
* 前端主题修改简化自Wordpress的Twenty eleven (2011)主题

## 安装使用
### 在本地调试使用
直接clone，在Decblog文件夹中找到manage.py，在shell中直接运行 `python manage.py runserver`。然后打开浏览器，输入localhost:8000看到页面。
### Nginx + uWSGI 部署
由于Decblog是一个标准WSGI Application，Decblog\decblog\wsgi.py中的Application是入口。

### 部署到新浪云

## 待改进之处
