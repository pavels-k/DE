import py4j.GatewayServer;

public class MathServer {
    public int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        MathServer server = new MathServer();
        GatewayServer gatewayServer = new GatewayServer(server);
        gatewayServer.start();
        System.out.println("Py4J Java сервер запущен...");
    }
}
