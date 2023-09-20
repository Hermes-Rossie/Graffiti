using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;

public class WallpaintManager : MonoBehaviour
{
    public GameObject[] wallpaints;
    // Start is called before the first frame update
    public ARSessionOrigin sessionOrigin;
    public ARRaycastManager raycastManager;
    public ARPlaneManager planeManager;
    private List<ARRaycastHit> raycastHits = new List<ARRaycastHit>();
    private void Update(){
        if(Input.GetTouch(0).phase==TouchPhase.Began){

            bool collision = raycastManager.Raycast(Input.GetTouch(0).position, raycastHits, TrackableType.PlaneWithinPolygon);

            if(collision){
                GameObject _object = Instantiate(wallpaints[0]);
                _object.transform.position = raycastHits[0].pose.position;
            }

            foreach(ARPlane plane in planeManager.trackables){
                plane.gameObject.SetActive(false);
            }
            planeManager.enabled = false;
        }
    }
}
