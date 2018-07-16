# 基于Django1.10.6搭建的博客



- 实现显示详情页，分类，归档，标签后端逻辑
  - 创建标签和文章的ORM模型（多对多关系）
  - 创建分类和文章的ORM模型（一对多关系）
  - 创建用户和文章的ORM模型（一对多关系）

- 使用自定义模板标签templatetags实现博客右侧归档，标签的显示
  - 使用template.Library()实现自定义标签来统计分类和归档数量，同时可以使用annotate函数筛选掉没有文章的分类和标签不显示
- 实现评论逻辑
  - 创建评论应用
  - 设计评论数据库模型
  - 评论表单设计
  - 评论视图函数设计并绑定URL
  - 前端渲染表单
  - 显示评论内容
- 实现文章使用markdown语法高亮显示同时实现文章阅读量显示
- 实现用户注册逻辑
  - 使用Profile模式拓展用户模型
  - 编写注册表单
  - 编写用户注册试图函数
  - 设置URL
  - 编写注册页面模板
- 实现用户登陆逻辑
  - 引入Django内置编写好的URL模型 
    -  登录：^accounts/login/$[name='login'] 
    -  登出：^accounts/logout/$[name='logout'] 
    -  修改密码：^accounts/password_change/$[name='password_change'] 
    -  修改密码成功：^accounts/password_change/done/$[name='password_change_done'] 
    -  重设密码：^accounts/password_reset/$[name='password_reset'] 
    -  重设密码成功：^accounts/password_reset/done/$[name='password_reset_done'] 
    -  重设账户：^accounts/reset/(?P<uidb64>[0-9A-Za-z_-]+)/(?P<token>[0-9A-Za-z]{1,13}[0-9A-Za-z]{1,20})/$[name='password_reset_confirm'
  - 设置模板路径
  - 编写登陆模板
  - 在基础模板中设置判断是否登陆逻辑
    -  {% if user.is_authenticated %} 
  - 实现注销登陆URL
  - 添加登陆访问限制
    - from django.contrib.auth.decorators import login_required
  - 实现密码修改逻辑
