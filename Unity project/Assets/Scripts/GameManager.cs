using UnityEngine;
using UnityEngine.UI;

public class GameManager : MonoBehaviour
{
    public GameObject spawnObject;
    public GameObject [] spawnPoints;
    public float timer;
    public float timeBetweenSpawns;
    public float speedMultiplier;
    public Text distanceUI;
    private float distance;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        distanceUI.text = "Distance: " + distance.ToString("F2");
        speedMultiplier += Time.deltaTime * 0.005f;
        
        timer += Time.deltaTime;
        
        distance += Time.deltaTime * 0.8f;
        
        if (timer > timeBetweenSpawns)
        {
            timer = 0;
          int randNum = Random.Range(0, 3);
          Instantiate(spawnObject, spawnPoints[randNum].transform.position, Quaternion.identity); 
        }
    }
}
