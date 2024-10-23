import os, re
import sublime
import sublime_plugin
import subprocess

class ConnectToSshCommand(sublime_plugin.TextCommand):
    cfgfile = os.path.join(os.path.expanduser("~"),'.vsublime.cfg.py')
    def load_config(self):
        if not os.path.isfile(self.cfgfile):
            with open(self.cfgfile, 'w', encoding='utf8') as f:
                demo = [
                    "# demo: ssh root@192.168.0.1 password"
                ]
                f.write('\n')
        with open(self.cfgfile, encoding='utf8') as f:
            data = f.read()
        r = []
        for i in data.splitlines():
            t = i.strip()
            if t and not t.startswith('#'):
                def rep(g): return g.group(1)
                a = re.sub(r'\{\{(.*?)\}\}', lambda g:"********", t)
                b = re.sub(r'\{\{(.*?)\}\}', rep, t)
                r.append([a, b])
        return r
    def load_ssh_key(self, name):
        try:
            pub = os.path.join(os.path.expanduser("~"), '.ssh', 'id_rsa.pub')
            if not os.path.isfile(pub):
                return
            with open(pub, encoding='utf-8') as f:
                pubcode = f.read()
                pc = re.findall(r'ssh-rsa [^ ]+', pubcode)
                if not pc:
                    raise Exception('no ssh-rsa')
                pc = pc[0]

            cmd = '[[ -f ~/.ssh/authorized_keys ]] || touch ~/.ssh/authorized_keys; grep -q "'+pc+'" ~/.ssh/authorized_keys || echo "'+pc+'" >> ~/.ssh/authorized_keys'
            cmd = cmd + ' ' + name
            print('---- 在登录进去后使用下面的命令行将本地的 ssh 公钥上传上去,下次连接则不虚要密钥就能登录 ----')
            print(cmd)
            print('--------')
        except:
            cmd = ""
        return cmd
    def run(self, edit):
        ssh_addresses = self.load_config()
        ssh_addresses.append(('open_config', 'open_config'))
        ssh_addresses.append(('terminus_open', 'terminus_open'))
        options = [name for name, _ in ssh_addresses]
        self.view.window().show_quick_panel(options, lambda index: self.on_done(index, ssh_addresses))

    def on_done(self, index, ssh_addresses):
        if index == -1: return
        command = ssh_addresses[index][1]
        if command == 'open_config':
            new_view = sublime.active_window().open_file(self.cfgfile)
            return
        if command == 'terminus_open':
            self.view.window().run_command("terminus_open", { "cwd": "${file_path}" })
            return
        cmd = []
        _cmds = command.split(' ')
        if _cmds[0] == 'ssh':
            sshk = self.load_ssh_key(_cmds[1])
            _cmds = _cmds[:2]
        cmd.extend(_cmds)

        self.view.window().run_command("terminus_open", {
            "cmd": cmd,
            "cwd": "${file_path}",
            "auto_close": False,
        })
