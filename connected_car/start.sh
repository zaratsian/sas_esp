export DFESP_HOME="/opt/sasinside/ESP31/SASEventStreamProcessingEngine/3.2.0"
export LD_LIBRARY_PATH="/opt/sasinside/ESP31/SASEventStreamProcessingEngine/3.2.0/lib" 

$DFESP_HOME/bin/dfesp_xml_server -model file:////home/sas/connected_car/model.xml -http-admin 61051 -http-pubsub 61052 -pubsub 61053 -messages $DFESP_HOME/etc/xml/messages -loglevel esp=trace &

sleep 10

python inject_dynamic.py &
