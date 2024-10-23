#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
import sys
import pymysql
import pandas as pd
import paramiko
import re
import os
import platform
import configparser

class Connection:

    def __init__(self, username='', password='', match_id='', verbose=False):
        self.__headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }
        self.resources = None
        self.__username = username
        self.__password = password
        self.__match_id = match_id
        if self.__login()['status'] == 0:
            self.__login_token = self.__login()['data']['token']
        else:
            print("log err:{}".format(self.__login()['message']))

        if self.__get_record()['status'] == 0:
            data = self.__get_record()['data']
            self.__uuid = data['match_info']['uuid']
            self.__module_list = [module['id'] for module in data['match_modules']]
            self.__owner_id = data['match_record']['id']
            self.__vr_manage_url_token = data['vr_manage_url']['token']

            if self.__get_playload()['status'] == 0:
                self.__playload = self.__get_playload()['data']['all_payload']
                # 清楚hosts之前的内容，windterm2.6.1已修复此bug
                # self.__setclear()
                self.__setvar()
                # 获取element_id和module_id的对应关系
                self.__element_module_dict = self.__get_module_elements(verbose)
            else:
                print("get playload err:{}".format(self.__get_playload()['message']))
        else:
            print("get record err:{}".format(self.__get_record()['message']))

    def __login(self):
        """
        获取登录token
        """
        url = "https://api-prod.qingjiao.art/uc/api/token/v2"
        params = {
            'username': self.__username,
            'password': self.__password,
        }
        res = requests.post(url, headers = self.__headers, params=params)
        data = json.loads(res.text)

        token = data['data']['token']
        return data

    def __get_record(self):
        """
        获取owner_id、match_id和管理token
        """
        self.__headers['Authorization'] = self.__login_token
        url = 'https://api-prod.qingjiao.art/api/match/{}/record'.format(self.__match_id)
        res = requests.get(url, headers = self.__headers)
        data = json.loads(res.text)
        # data['data']
        return data

    def __get_playload(self):
        """
        获取status接口的content数据
        """
        self.__headers['Authorization'] = self.__login_token
        url = 'https://api-prod.qingjiao.art/api/match/record/{}/payload'.format(self.__owner_id)
        res = requests.get(url, headers = self.__headers)
        data = json.loads(res.text)

        # data['data']
        return data

    def __get_resource_list(self):
        """
        获取竞赛资源列表
        owner_id: 拥有者的id
        """
        ret = []
        self.__headers['Authorization'] = self.__login_token
        url = 'https://api-prod.qingjiao.art/api/match/record/{}/resource/list'.format(self.__owner_id)
        res = requests.get(url, headers = self.__headers)
        data = json.loads(res.text)
        if data['status'] != 0:
            print(data['message'])
            return

        resources = data['data']['resources']
        for i, res in enumerate(resources):
            host_name = {}
            host_name['resource_name'] = ' '.join(res['content']['name'].split()).replace("/", "-")
            host_name['resource_id'] = str(res['id'])
            ret.append(host_name)

        return ret

    def __get_resource_status(self, url='https://api.region-bj02.qingjiao.link//api/v3/virtual-resource/all/status'):
        """
        获取竞赛资源的状态，包括ip、public_ip和password
        """
        ret = []
        # url = 'https://api.region-bj02.qingjiao.link//api/v3/virtual-resource/all/status'
        # url = 'https://api.region-zjk02.qingjiao.link//api/v3/virtual-resource/all/status'
        self.__headers['Authorization'] = self.__vr_manage_url_token
        data = {
            "content": self.__playload
        }
        res = requests.post(url, headers = self.__headers, data=data)
        data = json.loads(res.text)

        if data['code'] != 0:
            print(data['message'])
            return

        resources = data['data']
        for i, res in enumerate(resources):
            host_info = {}
            host_info['ip'] = res['ip']
            host_info['public_ip'] = res['public_ip']
            host_info['password'] = res['password']
            host_info['resource_id'] = str(res['extra'])
            ret.append(host_info)
        return ret

    def __get_element_list(self, module_id):
        """
        获取模块的组成id
        """
        self.__headers['Authorization'] = self.__login_token
        start_url = 'https://api-prod.qingjiao.art/api/match/record/{}/module/{}/element/list'.format(self.__owner_id, module_id)

        response = requests.get(url=start_url, headers=self.__headers)
        data = json.loads(response.text)
        if data['status'] != 0:
            print(data['message'])
            return
        #ret = ['{}:{}'.format(element['name'], element['id']) for element in data['data']['elements']]
        return data['data']['elements']

    def __get_module_elements(self, verbose=False):
        """
        获取所有的模块和组合id
        """
        ret = {}
        modules = self.__module_list
        for module_id in modules:
            elements = self.__get_element_list(module_id)
            for element in elements:
                ret[str(element['id'])] = str(module_id)
            elements_list = ['{}:{}'.format(element['name'], element['id']) for element in elements]
            if verbose:
                print("module: {}, elements: {}".format(module_id, elements_list))

        return ret

    def __get_element_detail(self, element_id):
        """
        获取竞赛中题目的内容
        """
        self.__headers['Authorization'] = self.__login_token
        module_id = self.__element_module_dict[element_id]
        start_url = 'https://api-prod.qingjiao.art/api/match/record/{}/module/{}/element/{}/detail'.format(self.__owner_id, module_id, element_id)

        response = requests.get(url=start_url, headers=self.__headers)
        data = json.loads(response.text)
        if data['status'] != 0:
            print(data['message'])
            return
        if not os.path.exists('./md/{}'.format(self.__match_id)):
            # 目录不存在，创建目录
            os.makedirs('./md/{}'.format(self.__match_id))

        # 保存单选题
        if 'content' in data['data']['element'].keys():
            contents = data['data']['element']['content']
            f = open('./md/{}/{}-{}-{}.sql'.format(self.__match_id, self.__match_id, module_id, element_id), 'w', encoding='utf8')
            for i, content in enumerate(contents):
                title = content['name']
                partA = content['options'][0]
                partB = content['options'][1]
                partC = content['options'][2] if len(content['options']) > 2 else ''
                partD = content['options'][3] if len(content['options']) > 3 else ''
                insert_sql = "INSERT INTO `bd_practice` VALUES (NULL, '{}', NULL, '{}', '{}', '{}', '{}', NULL, NULL);".format(title, partA, partB, partC, partD)
                # f.write(title + "," + partA + "," + partB + "," + partC + "," + partD + '\n')
                f.write(insert_sql + '\n')
            f.close()

        # 保存解答题
        if 'order_tasks' in data['data']['element'].keys():
            order_tasks = data['data']['element']['order_tasks']
            f = open('./md/{}/{}-{}-{}.md'.format(self.__match_id, self.__match_id, module_id, element_id), 'w', encoding='utf8')
            name_head =  data['data']['element']['name']
            description_head =  data['data']['element']['description']
            f.writelines("# " + name_head + "\n\n")
            f.writelines(description_head)
            f.writelines('\n\n---\n\n')
            for i, task in enumerate(order_tasks):
                name = task['name']
                description = task['description']
                f.writelines("## " + name + "\n\n")
                f.writelines(description)
                f.writelines('\n\n---\n\n')
                order_conditions = task['order_conditions']
                f.writelines("### 考核条件如下 :\n")
                for i, condition in enumerate(order_conditions):
                    name = condition['name']
                    condition_desc = condition['condition_desc']
                    recourseName = "、".join(condition['params'][0]['recourseName'])
                    f.writelines("{}.{}\n\n".format(i+1, name))
                    if name != condition_desc:
                        f.writelines(condition_desc+ "\n\n")
                    f.writelines("操作环境: " + recourseName + "\n\n")
            f.close()

    def __setvar(self, verbose=False):
        """
        获取对象的hostname和public_ip，写入本地hosts
        """
        df_name = pd.DataFrame(self.__get_resource_list())
        url_master = 'https://api.region-bj02.qingjiao.link//api/v3/virtual-resource/all/status'
        url_slave = 'https://api.region-zjk02.qingjiao.link//api/v3/virtual-resource/all/status'
        if len(self.__get_resource_status(url_master)) != 0:
            df_info = pd.DataFrame(self.__get_resource_status(url_master))
        else:
            df_info = pd.DataFrame(self.__get_resource_status(url_slave))

        df = pd.merge(df_name, df_info,on='resource_id')
        self.resources = df[[col for col in df.columns if col != 'resource_id']]
        # print(df[[col for col in df.columns if col != 'resource_id']])

        # 清除之前hosts已有的内容
        if platform.system() == 'Windows':
            host_file = "C:/Windows/System32/drivers/etc/HOSTS"
        else:
            host_file = "/etc/hosts"

        with open(host_file, 'r', encoding='utf8') as f:
            lines = f.readlines()
        if '# Qingjiao Host Start\n' in lines:
            lines = lines[:lines.index('# Qingjiao Host Start\n')]
            with open(host_file, 'w', encoding='utf8') as f:
                f.writelines(lines)

        # 写入新的hosts
        with open(host_file, 'a+', encoding='utf8') as f:
            f.write("# Qingjiao Host Start\n")
            for index, row in df.iterrows():
                #if row['resource_name'] in ['Hadoop-Hive-Spark', 'Hadoop-Spark', 'Hadoop-hive']:
                #    f.write(row['public_ip']+" "+"hadoop000\n")
                f.write(row['public_ip']+" "+row['resource_name']+"\n")

    def __setclear(self):
        """
        清除本地WindTerm的密钥记录,windter2.6.1已修复此bug
        """
        if platform.system() == 'Windows':
            sessions_file = 'D:/Portable/WindTerm_2.5.0/.wind/profiles/default.v10/terminal/user.sessions'
        with open(sessions_file, 'r', encoding='utf8') as f:
            lines = f.readlines()
        new_lines = []
        for line in lines:
            if not 'session.autoLogin' in line:
                new_lines.append(line)
        with open(sessions_file, 'w', encoding='utf8') as f:
            f.writelines(new_lines)

    def setbasic(self, cluster_list=['master', 'slave1', 'slave2'], verbose=False):
        """
        登录主机后的基本操作
        """
        # 远程执行setvar
        command = "cat > /usr/etx.txt <<EOF\n"
        for index, row in self.resources.iterrows():
            command = command + row['resource_name'] + "," + row['ip'] + "," + row['public_ip'] + "," + row['password'] + "\n"
        command = command + "EOF"

        for index, row in self.resources.iterrows():
            resource_name = row['resource_name']
            # 执行远程命令
            out,err = self.exec(resource_name=resource_name, command=command)

            if resource_name in cluster_list:
                # print("{}-cluster".format(resource_name))
                download_command = "curl -o /etc/profile.d/my.sh -O -L https://gitee.com/yiluohan1234/vagrant_bigdata_cluster/raw/master/resources/bdcompetition/cluster.sh"
                out, err = self.exec(resource_name=resource_name, command=download_command)
                out, err = self.exec(resource_name=resource_name, command="source /etc/profile")
                out, err = self.exec(resource_name=resource_name, command="setvar")
                # 设置ip
                out, err = self.exec(resource_name=resource_name, command='source /etc/profile && setip')
            else:
                # print("{}-single".format(resource_name))
                download_command = "curl -o /etc/profile.d/my.sh -O -L https://gitee.com/yiluohan1234/vagrant_bigdata_cluster/raw/master/resources/bdcompetition/single.sh && source /etc/profile"
                out, err = self.exec(resource_name=resource_name, command=download_command)

        print("setbasic success!")

    def setlocalbasic(self, cluster_list=['master', 'slave1', 'slave2'], verbose=False):
        """
        登录主机后的基本操作
        """
        # 远程执行setvar
        command = "cat > /usr/etx.txt <<EOF\n"
        for index, row in self.resources.iterrows():
            command = command + row['resource_name'] + "," + row['ip'] + "," + row['public_ip'] + "," + row['password'] + "\n"
        command = command + "EOF"

        for index, row in self.resources.iterrows():
            resource_name = row['resource_name']
            # 执行远程命令
            out,err = self.exec(resource_name=resource_name, command=command)

            if resource_name in cluster_list:
                # print("{}-cluster".format(resource_name))
                self.upload(resource_name, 'D:/javaEnv/vagrant_bigdata_cluster/resources/bdcompetition/cluster.sh', '/etc/profile.d/my.sh')
                out, err = self.exec(resource_name=resource_name, command="source /etc/profile")
                out, err = self.exec(resource_name=resource_name, command="setvar")
                # 设置ip
                out, err = self.exec(resource_name=resource_name, command='source /etc/profile && setip')
            else:
                # print("{}-single".format(resource_name))
                self.upload(resource_name, 'D:/javaEnv/vagrant_bigdata_cluster/resources/bdcompetition/single.sh', '/etc/profile.d/my.sh')
                out, err = self.exec(resource_name=resource_name, command="source /etc/profile")

        print("setbasic success!")

    def setenvbasic(self, cluster_list=['master', 'slave1', 'slave2'], verbose=False):
        """
        登录主机后的基本操作
        """
        # 远程执行setvar
        import os
        import bdcp
        package_path = os.path.dirname(bdcp.__file__)
        cluster_file = package_path + '\sh\cluster.sh'
        single_file = package_path + '\sh\single.sh'

        command = "cat > /usr/etx.txt <<EOF\n"
        for index, row in self.resources.iterrows():
            command = command + row['resource_name'] + "," + row['ip'] + "," + row['public_ip'] + "," + row['password'] + "\n"
        command = command + "EOF"

        for index, row in self.resources.iterrows():
            resource_name = row['resource_name']
            # 执行远程命令
            out,err = self.exec(resource_name=resource_name, command=command)

            if resource_name in cluster_list:
                # print("{}-cluster".format(resource_name))
                self.upload(resource_name, cluster_file, '/etc/profile.d/my.sh')
                out, err = self.exec(resource_name=resource_name, command="source /etc/profile")
                out, err = self.exec(resource_name=resource_name, command="setvar")
                # 设置ip
                out, err = self.exec(resource_name=resource_name, command='source /etc/profile && setip')
            else:
                # print("{}-single".format(resource_name))
                self.upload(resource_name, single_file, '/etc/profile.d/my.sh')
                out, err = self.exec(resource_name=resource_name, command="source /etc/profile")

        print("setbasic success!")

    def exec(self, resource_name, command):
        """
        远程执行命令
        """
        hostname_df = self.resources[self.resources['resource_name']==resource_name]
        hostname = hostname_df['public_ip'].values[0]
        port = '22'
        username = 'root'
        password = hostname_df['password'].values[0]
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=hostname, port=port, username=username, password=password)

            stdin, stdout, stderr = ssh.exec_command(command)
            out = stdout.read().decode('utf-8')
            err = stderr.read().decode('utf-8')
        except paramiko.AuthenticationException as auth_exception:
            print("Authentication failed: {}".format(auth_exception))
        except paramiko.SSHException as ssh_exception:
            print("SSH connection failed: {}".format(ssh_exception))
        except Exception as general_exception:
            print("An unexpected error occurred: {}".format(general_exception))
        finally:
            ssh.close()
        return out, err

    def check(self, resource_name, verbose=True, inplace=True):
        """
        获取远程的日志文件内容
        """
        hostname_df = self.resources[self.resources['resource_name']==resource_name]
        hostname = hostname_df['public_ip'].values[0]
        port = '22'
        username = 'root'
        password = hostname_df['password'].values[0]
        out, err = self.exec(resource_name=resource_name, command="echo $(ps -ef | grep aliyun-assist | grep aliyun-service | grep -v grep | awk '{print $8}'|xargs dirname)/log/aliyun_assist_main.log")
        # out, err = self.exec(resource_name=resource_name, command='source /etc/profile && getlog')
        file = out.replace('\n', '')

        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            client.connect(hostname, port, username, password)
            sftp_client = client.open_sftp()
            remote_file = sftp_client.open(file, "r")
            file_content = remote_file.readlines()
            # lines = [line for line in file_content if "https://cn-beijing.axt.aliyun.com/luban/api/v1/task/finish" in line]
            lines = [line for line in file_content if "/luban/api/v1/task/finish" in line]
            ret_list = []
            for line in lines:
                line_str = line.replace("\\", "")
                json_match = re.search(r'{\s*"status":\s*(-?\d+),\s*"message":\s*".*?"\s*}', line_str)
                if json_match:
                    status_json = json_match.group(0)
                    status_data = json.loads(status_json)
                    ret_list.append(status_data)
            # 去除无用信息并过滤空字典
            filtered_list = [{k: v for k, v in ret_data.items() if k not in ["status", "message"]} for ret_data in ret_list]


            if not os.path.exists('./md/{}'.format(self.__match_id)):
                # 目录不存在，创建目录
                os.makedirs('./md/{}'.format(self.__match_id))

            # 将数据进行转换
            if verbose and len(filtered_list) > 0:
                for ret_data in filtered_list:
                    if 'command' in ret_data:
                        command = ret_data["command"]
                        if command.strip().startswith("cat"):
                            file_name = ret_data["command"].split()[1].strip()
                            greps = [word.split()[-1] for word in command.split("|")[1:] if word.strip().startswith("grep")]
                            grep_string = ",".join(greps) if len(greps) > 0 else ''
                            keyword = ',' + ret_data['keyword'] if 'keyword' in ret_data else ''
                            str_string = ',' + ret_data['strs'] if 'strs' in ret_data else ''
                            file_path = '/'.join(file_name.split('/')[:-1])
                            ret_data['exec'] = "[ ! -d {} ] && mkdir -p {}; echo '{}{}{}' >> {}".format(file_path, file_path, grep_string, keyword, str_string, file_name)

                        if command.strip().startswith("head"):
                            file_name = ret_data["command"].split()[3].strip()
                            greps = [word.split()[-1] for word in command.split("|")[1:] if word.strip().startswith("grep")]
                            grep_string = ",".join(greps) if len(greps) > 0 else ''
                            keyword = ',' + ret_data['keyword'] if 'keyword' in ret_data else ''
                            str_string = ',' + ret_data['strs'] if 'strs' in ret_data else ''
                            file_path = '/'.join(file_name.split('/')[:-1])
                            ret_data['exec'] = "[ ! -d {} ] && mkdir -p {}; echo '{}{}{}' >> {}".format(file_path, file_path, grep_string, keyword, str_string, file_name)

                        if command.strip().startswith("grep"):
                            file_name = ret_data["command"].split()[2].strip()
                            command_key = ret_data["command"].split()[1].strip()
                            greps = [word.split()[-1] for word in command.split("|")[1:] if word.strip().startswith("grep")]
                            grep_string = ',' + ",".join(greps) if len(greps) > 0 else ''
                            keyword = ',' + ret_data['keyword'] if 'keyword' in ret_data else ''
                            str_string = ',' + ret_data['strs'] if 'strs' in ret_data else ''
                            file_path = '/'.join(file_name.split('/')[:-1])
                            ret_data['exec'] = "[ ! -d {} ] && mkdir -p {}; echo '{}{}{}{}' >> {}".format(file_path, file_path, command_key, grep_string, keyword, str_string, file_name)

                        if command.strip().startswith("file"):
                            if ret_data['keyword'] == 'Hierarchical Data Format':
                                file_name = command.split()[1]
                                download_command = "curl -o {} -O -L https://gitee.com/yiluohan1234/vagrant_bigdata_cluster/raw/master/resources/bdcompetition/demo.h5".format(file_name)
                                out, err = self.exec(resource_name=resource_name, command=download_command)
                                # self.upload(resource_name, 'D:/javaEnv/vagrant_bigdata_cluster/resources/bdcompetition/demo.h5', file_name)
                            else:
                                path_name = ret_data["command"].split()[1].strip()
                                keyword = ret_data['keyword'] if 'keyword' in ret_data else ''
                                str_string = ',' + ret_data['strs'] if 'strs' in ret_data else ''
                                ret_data['exec'] = "echo '{}{}' >> {}".format(keyword, str_string, path_name)

                        if command.strip().startswith("ls"):
                            dir_path = ret_data["command"].split()[1].strip()
                            keyword = ret_data['keyword'] if 'keyword' in ret_data else ''
                            str_string = '-' + ret_data['strs'] if 'strs' in ret_data else ''
                            file_name = dir_path + '/demo.' + keyword +  str_string
                            ret_data['exec'] = "touch {} ".format(file_name)
                    else:
                        if 'file' in ret_data:
                            str_string = ret_data['strs'] if 'strs' in ret_data else ''
                            ret_data['exec'] = "echo '{}' >> {}".format(str_string, ret_data['file'])
                        elif 'directory' in ret_data:
                            dir_path = ret_data['directory']
                            ret_data['exec'] = "mkdir -p {}".format(dir_path)

            # 节省时间，仅执行最新的命令
            # if inplace and len(filtered_list) > 0 and 'exec' in filtered_list[-1]:
            #     self.exec(resource_name=resource_name, command=filtered_list[-1]['exec'])
            if inplace:
                file_path = './md/{}/exec.txt'.format(self.__match_id)
                lines_set = {line.strip() for line in open(file_path, 'r', encoding='utf-8').readlines()} if os.path.exists(file_path) else set()

                for ret in filtered_list[-3:]:
                    if 'exec' in ret and ret['exec'] not in lines_set:
                        self.exec(resource_name=resource_name, command=ret['exec'])
                        with open(file_path, 'a+', encoding='utf-8') as file:
                            file.write(ret['exec'] + "\n")

            # 去重
            distinct_list = []
            for ret in filtered_list:
                if ret not in distinct_list:
                    distinct_list.append(ret)

            # 打印倒数3个JSON数据
            if len(filtered_list) > 0:
                for data in filtered_list[-3:]:
                    print(data)

            # 保存
            with open('./md/{}/{}.json'.format(self.__match_id, resource_name), 'w', encoding='utf-8') as f:
                json.dump(distinct_list, f, ensure_ascii=False, indent=4)

        except paramiko.AuthenticationException as auth_exception:
            print("Authentication failed: {}".format(auth_exception))
        except paramiko.SSHException as ssh_exception:
            print("SSH connection failed: {}".format(ssh_exception))
        except Exception as general_exception:
            print("An unexpected error occurred: {}".format(general_exception))
        finally:
            remote_file.close()
            client.close()

    def hostname(self, resource_name, hostname):
        hostname_df = self.resources[self.resources['resource_name']==resource_name]
        ip = hostname_df['public_ip'].values[0]
        if platform.system() == 'Windows':
            host_file = "C:/Windows/System32/drivers/etc/HOSTS"
        else:
            host_file = "/etc/hosts"

        with open(host_file, "r") as file:
            current_hosts_content = file.readlines()

        new_hosts_content = [line for line in current_hosts_content if not line.strip().endswith(hostname)]

        new_hosts_content.append("{} {}\n".format(ip, hostname))

        with open(host_file, "w") as file:
            file.writelines(new_hosts_content)

    def upload(self, resource_name, local_file_path, remote_file_path):
        """
        获取远程的日志文件内容
        """
        hostname_df = self.resources[self.resources['resource_name']==resource_name]
        hostname = hostname_df['public_ip'].values[0]
        port = '22'
        username = 'root'
        password = hostname_df['password'].values[0]
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname, port, username, password)
            sftp = client.open_sftp()
            # 上传本地文件到远程服务器
            # 报错Failure：sftp.put("/tmp/xx.py", "/tmp/xx.py")
            sftp.put(local_file_path, remote_file_path)
        except paramiko.AuthenticationException as auth_exception:
            print("Authentication failed: {}".format(auth_exception))
        except paramiko.SSHException as ssh_exception:
            print("SSH connection failed: {}".format(ssh_exception))
        except Exception as general_exception:
            print("An unexpected error occurred: {}".format(general_exception))
        finally:
            sftp.close()
            client.close()

    def download(self, resource_name, remote_file):
        """
        获取远程的日志文件内容
        """
        local_dir = './download/{}/'.format(self.__match_id)
        if not os.path.exists(local_dir):
            # 目录不存在，创建目录
            os.makedirs(local_dir)

        file_name = remote_file.split('/')[-1]
        local_file = local_dir + file_name
        hostname_df = self.resources[self.resources['resource_name']==resource_name]
        hostname = hostname_df['public_ip'].values[0]
        port = '22'
        username = 'root'
        password = hostname_df['password'].values[0]
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname, port, username, password)
            sftp = client.open_sftp()
            # 上传本地文件到远程服务器
            # 报错Failure：sftp.put("/tmp/xx.py", "/tmp/xx.py")
            sftp.get(remote_file, local_file)
        except paramiko.AuthenticationException as auth_exception:
            print("Authentication failed: {}".format(auth_exception))
        except paramiko.SSHException as ssh_exception:
            print("SSH connection failed: {}".format(ssh_exception))
        except Exception as general_exception:
            print("An unexpected error occurred: {}".format(general_exception))
        finally:
            sftp.close()
            client.close()

    def getsql(self, resource_name, sql_name):
        """
        获取sql文件
        """
        download_sql = "curl -o /root/{}.sql -O -L https://gitee.com/yiluohan1234/vagrant_bigdata_cluster/raw/master/resources/bdcompetition/sql/{}.sql && source /etc/profile".format(sql_name, sql_name)
        out, err = self.exec(resource_name=resource_name, command=download_sql)
        print("upload sql success！")

    def setssh(self):
        """
        windows和linux免密登录
        """
        if platform.system() == 'Windows':
            username = os.environ.get('USERNAME')
            id_rsa_path = 'C:/Users/{}/.ssh/id_rsa.pub'.format(username)
            ssh_known_file = 'C:/Users/{}/.ssh/known_hosts'.format(username)
            ssh_config_file = 'C:/Users/{}/.ssh/config'.format(username)
        else:
            id_rsa_path = '/root/.ssh/id_rsa.pub'
            ssh_known_file = '/root/.ssh/known_hosts'

        for index, row in self.resources.iterrows():
            resource_name = row['resource_name']
            self.upload(resource_name, id_rsa_path, '/root/id_rsa.pub')
            out, err = self.exec(resource_name, 'source /etc/profile && cat /root/id_rsa.pub >> ~/.ssh/authorized_keys && rm -rf /root/id_rsa.pub')

        # 清除之前已有的内容
        if platform.system() == 'Windows':
            with open(ssh_config_file, 'r', encoding='utf8') as f:
                lines = f.readlines()
            if '# Qingjiao Host Start\n' in lines:
                lines = lines[:lines.index('# Qingjiao Host Start\n')]
                with open(ssh_config_file, 'w', encoding='utf8') as f:
                    f.writelines(lines)

            # 写入新的ssh_config
            with open(ssh_config_file, 'a+', encoding='utf8') as f:
                f.write("# Qingjiao Host Start\n")
                for index, row in self.resources.iterrows():
                    f.write("Host " + row['resource_name'] + "\n")
                    f.write("    HostName " + row['public_ip'] + "\n")
                    f.write("    Port 22\n")
                    f.write("    User root\n")
                    f.write("    IdentityFile ~/.ssh/id_rsa\n\n")

        # 清除known中已存的信息
        with open(ssh_known_file, 'r', encoding='utf8') as f:
            lines = f.readlines()
        new_lines = []
        for line in lines:
            is_exist = False
            for index, row in self.resources.iterrows():
                resource_name = row['resource_name'].lower()
                if resource_name in line :
                    is_exist = True
                    break
            if not is_exist:
                new_lines.append(line)
        with open(ssh_known_file, 'w', encoding='utf8') as f:
            f.writelines(new_lines)

    def get_command(self, title):
        if platform.system() == 'Windows':
            username = os.environ.get('USERNAME')
            config_path = 'C:/Users/{}/.config.ini'.format(username)
        else:
            config_path = '/root/.config.ini'
        # 读取INI配置文件
        config = configparser.ConfigParser()
        config.read(config_path)

        # 获取配置
        host = config.get('MySQL', 'host')
        user = config.get('MySQL', 'user')
        passwd = config.get('MySQL', 'passwd')
        port = int(config.get('MySQL', 'port'))
        db_name = config.get('MySQL', 'db_name')
        ret = []
        try:
            db=pymysql.connect(host=host,user=user,passwd=passwd, port=port, db=db_name,charset='utf8')
            cursor = db.cursor()
            sql = "select * from bd_command where title like '%{}%'".format(title)
            cursor.execute(sql)
            data_list = cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            db.commit()
            db.close()
        for data in data_list:
            #print(data)
            ret.append({'type':data[1], 'title':data[2], 'command': data[3]})
        if len(ret) == 0:
            print("no data")
            return
        return ret

    def get_abcd(self, title):
        if platform.system() == 'Windows':
            username = os.environ.get('USERNAME')
            config_path = 'C:/Users/{}/.config.ini'.format(username)
        else:
            config_path = '/root/.config.ini'
        # 读取INI配置文件
        config = configparser.ConfigParser()
        config.read(config_path)

        # 获取配置
        host = config.get('MySQL', 'host')
        user = config.get('MySQL', 'user')
        passwd = config.get('MySQL', 'passwd')
        port = int(config.get('MySQL', 'port'))
        db_name = config.get('MySQL', 'db_name')
        ret = []
        try:
            db=pymysql.connect(host=host,user=user,passwd=passwd, port=port, db=db_name,charset='utf8')
            cursor = db.cursor()
            sql = "select * from bd_practice where title like '%{}%'".format(title)
            cursor.execute(sql)
            data_list = cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            db.commit()
            db.close()
        for data in data_list:
            #print(data)
            ret.append({'type':data[2], 'answer':data[7], 'title':data[1], 'A':data[3], 'B':data[4], 'C':data[5], 'D':data[6]})
        if len(ret) == 0:
            print("no data")
            return
        return ret

    def init_mysql_config(self):
        """
        初始化mysql配置文件
        """
        if platform.system() == 'Windows':
            username = os.environ.get('USERNAME')
            config_path = 'C:/Users/{}/.config.ini'.format(username)
        else:
            config_path = '/root/.config.ini'
        with open(config_path, 'w', encoding='utf8') as f:
            f.write("[MySQL]\n")
            f.write("host=localhost\n")
            f.write("user=root\n")
            f.write("passwd=199037wW\n")
            f.write("port=3306\n")
            f.write("db_name=hongya\n")

    def get_exam_content(self):
        """
        获取竞赛中所有的模块的内容
        """
        for element_id in self.__element_module_dict.keys():
            self.__get_element_detail(element_id)

    def clear(self):
        """
        删除my.sh
        """
        for index, row in self.resources.iterrows():
            resource_name = row['resource_name']
            # 执行远程命令
            out, err = self.exec(resource_name=resource_name, command='rm -rf /etc/profile.d/my.sh')