output_file = open('/home/breno/aeroporto.txt', 'w')
for f in layer.getFeatures():
  geom = f.geometry()
  line = '%s, %s, %f, %f\n' % (f['name'], f['iata_code'],
          geom.asPoint().y(), geom.asPoint().x())
  unicode_line = line.encode('utf-8')
  output_file.write(unicode_line)
output_file.close()
         