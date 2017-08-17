# -*- mode: python -*-

block_cipher = None


a = Analysis(['F:\\PythonProject\\dpc_spider\\connectionsqlserver.py', 'F:\\PythonProject\\dpc_spider\\ProxyIP.py', 'F:\\PythonProject\\dpc_spider\\saveerrorlogs.py', 'F:\\PythonProject\\dpc_spider\\SpiderCHData.py'],
             pathex=['F:\\PythonProject\\dpc_spider'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='connectionsqlserver',
          debug=False,
          strip=False,
          upx=True,
          console=True )
