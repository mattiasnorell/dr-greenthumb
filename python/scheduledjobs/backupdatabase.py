import datetime
from shutil import copyfile
import sys
from os.path import isfile, join
import glob
import os
from core.Settings import Settings
from scheduledjobs.jobbase import JobBase

class BackupDatabase(JobBase):
	def __init__(self):
		super().__init__()
	
	def run(self):
		self.deleteOldBackups()
		self.copyBackup()

	def deleteOldBackups(self):
		# Delete old backups
		maxBackups = self.settings.config.backup.max_database_backups
		backupDir = self.settings.config.backup.database

		files = glob.glob(backupDir + "*.db")
		files.sort(key=os.path.getmtime, reverse=True)

		for num in range(maxBackups, len(files)):
			os.remove(files[num])

	def copyBackup(self):
		# Copy new backup
		backupDir = self.settings.config.backup.database
		source = self.settings.config.database.path
		dateTime = datetime.datetime.now().strftime('%Y-%m-%d')
		dest = backupDir + 'greenhouse_backup_' + dateTime + '.db'

		copyfile(source, dest)
		self.logger.log("Database backup created")