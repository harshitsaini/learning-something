import java.util.*;
import org.apache.kafka.clients.producer.Callback;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;

class test {

    private static class DemoProducerCallBack implements Callback{
        @Override
        public void onCompletion(RecordMetadata recordMetadata, Exception e){
            if (e != null) {
                e.printStackTrace();
            }
        }
    }
    public static void main(String[] args){

        Properties kafkaProps = new Properties();
        kafkaProps.put("bootstrap.servers", "localhost:9092");
    
        // Serializer for message key       
        // kafkaProps.put(
        //     "key.serializer",
        //     "org.apache.kafka.common.serialization.StringSerializer");
        kafkaProps.put("key.serializer",
                       "io.confluent.kafka.serializers.KafkaAvroSerializer");
        
        // // Serializer for message value
        // kafkaProps.put(
        //     "value.serializer",
        //     "CustomerSerializer");
        kafkaProps.put("value.serializer",
                       "io.confluent.kafka.serializers.KafkaAvroSerializer");

    
        String schemaUrl = "http://localhost:8081/schemas/ids/263";
  
        kafkaProps.put("schema.registry.url", schemaUrl);

        KafkaProducer producer = new KafkaProducer<String, String>(kafkaProps); 

        DemoProducerCallBack producerCallback = new DemoProducerCallBack();

        String customerName = args[0];

        Customer c1 = new Customer(123, customerName); 

        ProducerRecord<String, Customer> record =
            new ProducerRecord<>("test", "key_hello", c1);

        // ProducerRecord<String, String> record =
        //     new ProducerRecord<>(
        //         "test",
        //         "key_hello",
        //         "new_value_hello");

        try {
            producer.send(record, producerCallback);
            producer.close();
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    };

};