#!python3
#encoding:utf-8
import os.path
import subprocess

def Main():
	if -1 != Create():
		Commit()

def CreateInfo():
	print('ユーザ名: ')
	print('メアド: ')
	print('SSH HOST: ')
	print('リポジトリ名: ')
	print('説明: ')
	print('URL: ')
	print('リポジトリ情報は上記のとおりで間違いありませんか？[y/n]')

def Create():
	if os.path.exists(".git"):
		return 0
	answer = ''
	while '' == answer:
		CreateInfo()
		answer = input()
		if 'y' == answer or 'Y' == answer:
			CreateCommands()
			return 0
		elif 'n' == answer or 'N' == answer:
			print('conf.iniを編集して再度やり直してください。')
			return -1
		else:
			answer = ''

def CreateCommands():
	print('(リポジトリ作成する)')
	# subprocess.call('git init')
	# ...

def CommitInfo():
	print('リポジトリ名： ')
	print('説明: ')
	print('URL: ')
	print('----------------------------------------')
	#res = subprocess.call('git add -n .')
	print('(addするファイル一覧を表示する)')
	print('commit,pushするならメッセージを入力してください。Enterかnで終了します。')
	print('サブコマンド    n:終了 e:編集 d:削除 i:Issue作成')

def Commit():
	CommitInfo()
	answer = input()
	if '' == answer or 'n' == answer or 'N' == answer:
		print('何もせず終了します。')
	elif 'e' == answer or 'E' == answer:
		print('(リポジトリ編集する)')
	elif 'd' == answer or 'D' == answer:
		print('(リポジトリ削除する)')
	elif 'i' == answer or 'I' == answer:
		print('(Issue作成する)')
	else:
		CommitCommands()
		Aggregate()

def CommitCommands():
	print('commit,push')
	# subprocess.call("git commit -m 'message'")
	# ...

def Aggregate():
	print('(集計を表示する)')

Main()
