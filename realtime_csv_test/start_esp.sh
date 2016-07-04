
export DFESP_HOME="/home/dtz001/SASEventStreamProcessingEngine/3.2.0/"
export LD_LIBRARY_PATH="/home/dtz001/SASEventStreamProcessingEngine/3.2.0/lib"

$DFESP_HOME/bin/dfesp_xml_server -model file:////home/dtz001/sas/zprojects/esp_simple_csv_tester/model.xml -http-admin 61051 -http-pubsub 61052 -pubsub 61053 -messages $DFESP_HOME/etc/xml/messages -loglevel trace &

$DFESP_HOME/bin/dfesp_fs_adapter -k pub -h "dfESP://localhost:61053/Project/CQ/Data_Input?snapshot=true" -f data.csv -t csv &
