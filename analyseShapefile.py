from PyQt4.QtGui import *

def analyse_shapefile():
    filename = QFileDialog.getOpenFileName(iface.mainWindow(), "Select Shapefile","~","*.shp")
    if not filename:
        print "Cancelled"
        return
        
    registry = QgsProviderRegistry.instance()
    provider = registry.provider("ogr", filename)
    
    if not provider.isValid():
        print ("Invalid shapefile")
        return
        
    attr_names = []
    for field in provider.fields():
        attr_names.append(field.name())
        
    crs = provider.crs()
    calculator = QgsDistanceArea()
    calculator.setSourceCrs(crs)
    calculator.setEllipsoid(crs.ellipsoidAcronym())
    calculator.setEllipsoidalMode(crs.geographicFlag())
    
    tot_lenght = 0
    tot_area = 0
    
    for feature in provider.getFeatures(QgsFeatureRequest()):
        if "name" in attr_names:
            feature_label = feature.attribute("name")
        elif "Name" in attr_names:
            feature_label = feature.attribute("Name")
        elif "NAME" in attr_names:
            feature_label = feature.attribute("NAME")
        else:
            feature_label = str(feature.id())
    
        geometry = feature.geometry()
        
        if geometry.type() == QGis.Line:
            length = int(calculator.measure(geometry)/100)
            tot_length = tot_length + length
            feature_info = "line of length %d kilometres" % length
        elif geometry.type() == QGis.Polygon:
            area = int(calculator.measure(geometry)/1000000)
            tot_area = tot_area + area
            feature_info = "polygon of area %d square.kilometres" % area
        else:
            geo_type = qgisVectorGeometryType(geometry.type())
            feature_info = "geometry of type %s" % geom_type
            
        print "%s: %s" % (feature_label,feature_info)
    
    print "Total length of all line features: %s" % tot_length
    print "Total area of all polygon features: %s" % tot_area
        
           
analyse_shapefile()

