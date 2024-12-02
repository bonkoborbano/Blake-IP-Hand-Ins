using System;
using System.Net;
using System.Net.Sockets;
using UnityEngine;
using System.Threading;

public class MyListener : MonoBehaviour
{
    private Thread listenerThread;
    public int connectionPort = 25001;
    private TcpListener server;
    private TcpClient client;
    private volatile bool running; // Ensures thread-safe access to this variable
    public int dataReceived;

    private static MyListener instance;

    
    void Awake()
    {
        // Singleton pattern to ensure only one instance exists
        if (instance == null)
        {
            instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
            return;
        }
    }
    
    

    void Start()
    {
        StartListenerThread();
    }

    private void StartListenerThread()
    {
        if (listenerThread == null || !listenerThread.IsAlive)
        {
            running = true;
            listenerThread = new Thread(ListenerLoop)
            {
                IsBackground = true // Allows Unity to close the app without hanging
            };
            listenerThread.Start();
        }
    }

    private void ListenerLoop()
    {
        try
        {
            server = new TcpListener(IPAddress.Any, connectionPort);
            server.Start();
            Debug.Log("Server started, waiting for connection...");

            client = server.AcceptTcpClient();
            Debug.Log("Client connected!");

            while (running)
            {
                if (client != null && client.Connected)
                {
                    NetworkStream nwStream = client.GetStream();
                    if (nwStream.DataAvailable)
                    {
                        byte[] buffer = new byte[sizeof(int)];
                        int bytesRead = nwStream.Read(buffer, 0, buffer.Length);

                        if (bytesRead == sizeof(int))
                        {
                            dataReceived = BitConverter.ToInt32(buffer, 0);
                            Debug.Log("Received integer: " + dataReceived);
                        }
                    }
                }
            }
        }
        catch (SocketException e)
        {
            if (running)
            {
                Debug.LogError($"Socket exception: {e.Message}");
            }
        }
        finally
        {
            StopServer();
        }
    }

    private void StopServer()
    {
        running = false;
        client?.Close();
        server?.Stop();
        Debug.Log("Server stopped.");
    }

    void OnDestroy()
    {
        CleanUp();
    }

    void OnApplicationQuit()
    {
        CleanUp();
    }

    private void CleanUp()
    {
        running = false;
        if (listenerThread != null && listenerThread.IsAlive)
        {
            listenerThread.Join(); // Wait for the thread to finish
        }
    }
}