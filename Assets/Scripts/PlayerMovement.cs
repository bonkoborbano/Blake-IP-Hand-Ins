using UnityEngine;
using UnityEngine.SceneManagement;

public class PlayerMovement : MonoBehaviour
{
    private Rigidbody2D rb;
    public float jump; // Adjust as needed
    private bool isGrounded;
    public MyListener _myListener;
    public Animator anim;

    private void Awake()
    {
        rb = GetComponent<Rigidbody2D>();
        _myListener = FindObjectOfType<MyListener>();

        if (_myListener == null)
        {
            Debug.LogError("MyListener component not found in the scene.");
        }
    }

    private void OnCollisionEnter2D(Collision2D other)
    {
        if (other.gameObject.CompareTag("Ground"))
        {
            isGrounded = true;
            Debug.Log("Grounded!");
        }
    }

    private void OnCollisionExit2D(Collision2D other)
    {
        if (other.gameObject.CompareTag("Ground"))
        {
            isGrounded = false;
            Debug.Log("Not Grounded!");
        }
    }

    void Update()
    {
        Debug.Log("Data in MovementScript: " + _myListener.dataReceived);

        if (_myListener.dataReceived == 5 && isGrounded)
        {
            rb.AddForce(Vector2.up * jump);
            Debug.Log("JUMP!");
        }
        
        
        if (_myListener.dataReceived == 2)
        {
            anim.SetBool("Slide", true);
        }
        else if (_myListener.dataReceived == 0)
        {
            anim.SetBool("Slide", false);
        }
        
    }

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Enemy"))
        {
            SceneManager.LoadScene("SampleScene");
        }
    }
}