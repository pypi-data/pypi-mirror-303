#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 24.10.21
import os,sys, cns
import winsound
import sqlite3, re  #知鸟用

class ProX(cns.sqlX, cns.SQLstrX):
    sqld = {}
    tmpl = {}
    def __init__(self, init_path='', **kwargs):
        SQLD = kwargs.get('sqld', {})
        TMPL = kwargs.get('tmpl', {})
        ProX.sqld.update(SQLD)
        ProX.tmpl.update(TMPL)

        self.str = init_path
        self.Beep = kwargs.get('Beep', None) # 提示音
        if self.Beep:
            winsound.Beep(800, 500) # 评率, 发生时长毫秒

        kwargs = dict(
            conn = kwargs.get('conn', 0),
            usr = kwargs.get('usr', 'test'),
            pwd = kwargs.get('pwd', 'test'),
            host = kwargs.get('host', 'localhost'),
            db = kwargs.get('db', 'test'),
            port = kwargs.get('port', 3306),
            tmpl = ProX.tmpl
        ) 
        super().__init__(**kwargs)  # 调用父类的初始化方法 

        self.status = 0             # 系统状态 0 正常，其他不正常
        self.file_path = os.path.realpath(sys.argv[0])   # 文件完整路径
        self.file_dir = os.path.dirname(self.file_path)       # 文件所在目录
        self.file_name = os.path.splitext(os.path.basename(self.file_path)) #文件名

        self.timex = cns.DateTimeX(kwargs.get('date', None)) # 时间对象
        self.cmdx = cns.cmdX(self.file_dir)
        self.strx = cns.strX()
        self.rpa = cns.strX()

    def __getitem__(self, index):
        '''
        # 创建
        t表维度_str = ",IFNULL({t1}.`GMV`, 0) as 'GMV{t2}"
        SQLD['t表维度'] = cns.ProX(t表维度_str)
        
        #调用  {param[t表维度][t3,.t3]}
        #结果  ,IFNULL(t1.`GMV`, 0) as 'GMV.t3'
        '''
        lst = index.split(',')
        tdic = {}
        for index, value in enumerate(lst):
            tdic['t'+str(index+1)]=value
        return self.str.format(**tdic)

    def to_db(self, **kwargs):
        '''EXCEL, csv 文档写入数据库, 增加复制模板'''
        kwargs = dict(       
            path = kwargs.get('path', ''),       # 读取路径
            header = kwargs.get('header', 0),    # 表头行
            ydrop = kwargs.get('ydrop', 0),      # 删除列
            xdrop = kwargs.get('xdrop', 0),      # 删除行，合计
            mode = kwargs.get('mode', 'append'), # 模式: 增量|覆盖|覆盖+增量(多文件单表)  append | replace | repapp
            recol = kwargs.get('recol', 0),      # 需修改字段名
            columns = kwargs.get('columns', 0),  # 选择字段
            fnames = kwargs.get('fnames', 0),    # 文件名
            ext = kwargs.get('ext', None),       # 文件扩展名            
            tname = kwargs.get('tname', None),   # 目标表名Mysql
            addcol = kwargs.get('addcol', 0),    # 增加列，通常是日期
            delrec = kwargs.get('delrec', 0),    # 根据表中某一列关键字删除数据,防止重复
            filt_col_str = kwargs.get('filt_col_str', ['\n',',',' ','%']),  # 过滤字段中字符
            converters = kwargs.get('converters', None),  # 可以在读取的时候对列数据进行变换 converters={"编号": lambda x: int(x) + 10})
            # EXCEL部分
            sheet_name = kwargs.get('sheet_name', 0), # 读 取EXCEL插页名字 数字按插页索引,字符串按插页名字
            # csv 部分 -S
            sep = kwargs.get('sep', ',\t'),      # 分隔符
            dtype = kwargs.get('dtype', None),   # 指定字段的类型  {'c1':np.float64, 'c2': str})        
            encoding = kwargs.get('encoding', 'gb18030'),   # 字符编码 tab  'utf-16'
            engine = kwargs.get('engine', 'python'), # 解释引擎
            
            # 本类定义
            fm_copy = kwargs.get('fm_copy', 0),  # 复制表
            del_tab = kwargs.get('del_tab', 0),  # 删除 tname  
            )
        
        if self.status == 0:            
            fm_copy = kwargs.get("fm_copy", 0)   # 复制的模板表
            tname = kwargs.get("tname", None)    # 到目标表
            del_tab = kwargs.get("del_tab", 0)   # 删除表， 默认0 不删除
            
            if fm_copy:
                print('\n复制:', fm_copy)
                super().copy_tab(fm_copy, tname, del_tab=1)  # 复制表结构前--先删除表
            
            if del_tab:
                super().del_tab(tname)  # 删除表                 
            super().to_db(**kwargs)     # 写表
         
    def run_sqls(self, run_sql, SQLD=None):        
        ''' 批量执行SQL '''
        if SQLD==None:
            SQLD=self.sqld
            
        for sql_nm, param in run_sql.items():
            sql_nm = sql_nm.split('.')  # 取任务名
            print('执行:', sql_nm[0])
            if len(sql_nm) == 1:
                task_nm = sql_nm[0]
            else:
                task_nm = sql_nm[1]
            self.to_pro(task_nm, param=param, sqld=SQLD) # 任务名称, 参数, 主脚本  setdefault(key[,default])

    def to_pro(self, task_nm='任务名空', **kwargs):
        ''' 数据处理 '''
        if self.status == 0:            
            tname = kwargs.get("tname", None)   # 目标表            
            fm_copy = kwargs.get("fm_copy", 0)  # 复制表          
            del_tab = kwargs.get("del_tab", 0)  # 删除表， 默认0 不删除                  
            param = kwargs.get("param", None)   # 到目标表            
            sqld = kwargs.get("sqld", 0)        # 待执行的SQL            
            ren_tab = kwargs.get("ren_tab", 0)  # 重命名表名 

            to_copy = kwargs.get("to_copy", 0) 
            
            if del_tab:
                super().del_tab(tname)  # 删除表                
            if fm_copy:
                super().copy_tab(fm_copy, tname, del_tab=1) # 复制表            
            if sqld:
                sql = sqld[task_nm]

                param.setdefault("s1", '') # select * from 
                param.setdefault("s2", '') # select * from 

                param.setdefault("w1", '') # where1
                param.setdefault("w2", '') # where2
                if(param.get('w2')):
                    param.setdefault("(", '(')
                    param.setdefault(")", ')')
                else:
                    param.setdefault("(",'')
                    param.setdefault(")", '')
                    
                param.setdefault("s", param.get('s1','None')) 
                param.setdefault("w", param.get('w1','None')) # where1 
                param.setdefault("icol", '') # where2 
                param.setdefault("on2", param.get('on','None')) #
                param.setdefault("onMore", '') # select * from 
                             
                sql = sql.format(tname=tname, param=param, p=param)  # 格式化SQL ,3参数过度用
                super().run_sql(sql, task_nm = task_nm)              # 执行SQL

            if ren_tab:
                super().ren_tab(to_copy, ren_tab)           # 修改表名, 用于临时表修改正式表名


    def sql_make(self, **kwargs):
        ''' 生产SQL '''
        file_nm = kwargs.get("file_nm", '')    # 输出的文件名          
        sql_head = kwargs.get("sql_head", '')  # SQL 头部
        sql_main = kwargs.get("sql_main", '')  # SQL需要重复的核心部分  
        sql_tail = kwargs.get("sql_tail", '')  # SQL 尾部
        params = kwargs.get("params", '')      # SQL 传参
        interval= kwargs.get("interval", 'UNION ALL')      # 间隔

        txt_obj = cns.TextX(f"{self.file_dir}/{file_nm}")
        txt_obj.write(sql_head)        # 创建文档
        for index, value in enumerate(params):
            if index:
                txt_obj.append(interval)
            sql_temp = sql_main.format(param=value, p=value)
            txt_obj.append(sql_temp)    # 循环增加
        txt_obj.append(sql_tail)        # 尾部
        return txt_obj
        
    def paste(self, **kwargs):
        ''' SQL 粘贴数据到指定插页单元格'''
        sql = kwargs.get("sql", '')            # sql代码
        param = kwargs.get("param", '')        # sql参数
        excel = kwargs.get("excel", '')        # excel对象
        sheet = kwargs.get("sheet", '')        # 插页名称
        paste_xy = kwargs.get("paste_xy", '')  # 粘贴位置
        header = kwargs.get("header", 0)       # 是否带表头

        sql = sql.format(param=param, p=param)          
        df1 = self.read_sql(sql)               # data_type="list" 
        excel.set_sheet(sheet)
        excel.paste(df1, paste_xy, header=header)  # 粘贴(数据, 粘贴位置, 是否要表头)


    def __del__(self):
        if self.Beep:    
            winsound.Beep(900, 600) # 提示音(频率, 发生时长毫秒)
    
    
    # ----------------- sqld --------------------------24.09.27
    sqld['更新'] = "UPDATE `{p[t]}` SET {p[set]}"

    sqld['更新JOIN'] = ''' 
    UPDATE `{p[t]}` t1
    LEFT JOIN {p[(]}{p[s2]} `{p[f]}` {p[w2]}{p[)]} t2
    ON t1.`{p[on]}` = t2.`{p[on2]}` {p[onMore]}
    SET {p[set]}
    {p[w1]}
    '''

    sqld['SELECT建表'] = '''
    DROP TABLE IF EXISTS `{p[t]}`;
    CREATE TABLE `{p[t]}` AS
    SELECT
    {p[s]}
    FROM `{p[f]}` 
    {p[w]};
    '''

    sqld['插入'] = '''
    INSERT INTO `{p[t]}` 
    ({p[icol]})
    SELECT 
    {p[s]}
    FROM `{p[f]}` 
    {p[w]}
    '''
    sqld['创建索引'] = "CREATE INDEX 新索引 ON `{p[t]}` ({p[i]})"
    sqld['删除'] = "DELETE FROM `{p[t]}` WHERE {p[w]} "
    
    sqld['添加字段'] = "ALTER TABLE `{p[t]}` ADD COLUMN {p[col]}"      # {'t':'目标表', 'col':"`实际_商品GMV_自营`"}
    sqld['删除字段'] = "ALTER TABLE `{p[t]}` DROP COLUMN {p[col]}"     # {'t':'目标表', 'col':"`实际_商品GMV_自营` double(18,6) DEFAULT NULL"}
    sqld['修改字段'] = "ALTER TABLE `{p[t]}` CHANGE COLUMN {p[col]}"   # {'t':'目标表', 'col':"`实际_商品GMV_自营` `修改后的名字` double(18,6) DEFAULT NULL"}


    # ----------------- tmpl --------------------------24.9.27
    tmpl['select'] = {'头部':'select \n', '模板':"{连接2} `{值}`",  '连接':','}
    tmpl['col'] = { '模板': "{连接2}`{值}`",  '连接':','}
    tmpl['strin'] = { '模板': "{连接2}'{值}'",  '连接':','}
    tmpl['sum'] = { '模板': "{连接2}{名字}(`{值}`) as '{值}'",  '连接':','}
    tmpl['max'] = { '模板':"{连接2}{名字}(`{值}`) as '{值}'",  '连接':','}
    tmpl['on'] = { '模板': "{连接2} t0.`{值}`= t{计数}.`{值}`",  '连接':' AND '}        
    tmpl['增数据'] = {'头部':'INSERT INTO `{表名}` (\n',    '模板': "{连接}`{值}`", '连接':',',   '尾部':') VALUES ({值})'  }
    tmpl['删数据'] = {'模板':'DELETE FROM `{{表名}}` WHERE `品类`= {值};'}
    tmpl['改数据'] = {'模板':"UPDATE `{{表名}}` SET  `品类`='测试', `品牌`='1' WHERE `品类`= {值};"}
    tmpl['增索引'] = { '头部':'CREATE INDEX {索引名} ON {表名}(\n', '模板':"{连接}`{值}`", "连接":',', '尾部':')'}
    tmpl['删索引'] = { '头部':'', '模板':" DROP INDEX {值} ON {{表名}};"}
    tmpl['建表'] = { '头部':'CREATE TABLE {表名} (\n', '模板':"{连接2}`{值}` {{{值}_数据类型}}" , '连接':',', '尾部':'\n)'}    
    tmpl['删表'] = {'模板':"DROP TABLE IF EXISTS `{值}` ;"}
    tmpl['增字段'] = {'头部':'ALTER TABLE {表名}\n', '模板':"{连接2} ADD `{值}` {{{值}_数据类型}}", '连接':','}
    tmpl['删字段'] = {'头部':'ALTER TABLE {表名}\n', '模板':"{连接2} DROP COLUMN `{值}`", '连接':','}
    tmpl['改字段'] = {'头部':'ALTER TABLE {表名}\n', '模板':"{连接2} CHANGE COLUMN  {值} {{{值}_新字段名}}  {{{值}_数据类型}} ", '连接':','}
    tmpl['内连接'] = {'头部':'INNER JOIN {表名} ON\n', '模板':"{连接2} t0.`{值}`= t{计数}.`{值}`",  '连接':' AND '}
    tmpl['左连接'] = {'头部':'LEFT JOIN {表名} ON\n', '模板':"{连接2} t0.`{值}`= t{计数}.`{值}`",  '连接':' AND '}
    tmpl['右连接'] = {'头部':'RIGHT JOIN {表名} ON\n', '模板':"{连接2} t0.`{值}`= t{计数}.`{值}`",  '连接':' AND '}
    tmpl['全连接'] = {'头部':'RFULL OUTER JOIN  {表名} ON\n', '模板':"{连接2} t0.`{值}`= t{计数}.`{值}`",  '连接':' AND '} 


if __name__ == '__main__':
    x = ProX()
    print(x.sum("1,2,3"))