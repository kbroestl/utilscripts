#! /usr/bin/env python

"""
Fetch all the files out of the defunct DB
direct fetch, circumvent the web front end.
"""

from sqlalchemy import create_engine, MetaData, Table, select, insert, delete, text

"""
Local Settings on the dead Database
""""
DATABASE_ADAPTER = 'mysql'
DATABASE_HOST = 'localhost'
DATABASE_NAME = ''
DATABASE_USER = ''
DATABASE_PASSWORD = ''

def main():
	# would normally hook into command line options, etc.
	# sanity check
	# then...
	fetchlist()

def fetchlist():
	source = '%s://%s:%s@%s/%s' % (DATABASE_ADAPTER, DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_NAME)
	engine = create_engine( source )
	meta = MetaData(engine)
	"""
	There's an issue with the data -- the file_content stream causes misbehavior for mass exports
	Use a specific filename if you know it if you're really looking for something in particular
	"""
	sql = text("""
		select a.asset_id, i.filename, a.filetype, a.file_content, a.version from T_Asset a

		Inner Join T_AssetIndex i
			on i.id = a.index_id and i.version_live = a.version 

		where a.filename <> ''
		
		order by a.filename;
		""")
	result_set = [dict(r) for r in engine.execute(sql)]
	
	for row in result_set:
		print 'fetching %s, version %s' % (row['filename'], row['version'])
		handle = open(row['filename'], 'wb')
		handle.write(row['file_content'])

		handle.close()



if __name__ == '__main__':
	main()
