using UnityEngine;
using UnityEngine.SceneManagement;
public class NextScene : MonoBehaviour
{
    
    public void LoadNextScene()
    {
        SceneManager.LoadScene("SampleScene");
    }
    
    public void LoadMenu()
    {
        SceneManager.LoadScene("StartScreen");
    }
    
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
