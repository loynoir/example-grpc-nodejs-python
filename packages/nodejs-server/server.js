var messages = require('../generated-helloworld/generated/ts/helloworld_pb.js');
var services = require('../generated-helloworld/generated/ts/helloworld_grpc_pb.js');
var grpc = require('@grpc/grpc-js');
function sayHello(call, callback) {
  var reply = new messages.HelloReply();
  reply.setMessage('Hello ' + call.request.getName());
  callback(null, reply);
}
function main() {
  var server = new grpc.Server();
  server.addService(services.GreeterService, { sayHello: sayHello });
  server.bindAsync('0.0.0.0:50051', grpc.ServerCredentials.createInsecure(), () => {
    server.start();
  });
}
main();
