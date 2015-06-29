#include "Iw2D.h"
#include "input.h"
#include "audio.h"
int main() {
    Iw2DInit();
    g_pInput = new Input();
    CIw2DImage* image_1 = Iw2DCreateImage("textures/gem4.png");
	CIw2DImage* image_2 = Iw2DCreateImage("textures/gem3.png");
    CIwFVec2    image_position = CIwFVec2::g_Zero;

	int displayWidth = Iw2DGetSurfaceWidth();
	int displayHeight = Iw2DGetSurfaceHeight();
    
	while (!s3eDeviceCheckQuitRequest()) {
        g_pInput->Update();						// Update input system
        Iw2DSurfaceClear(0xff000000);			// Clear the drawing surface
		Iw2DSetColour(0xffffffff);
		Iw2DFillRect(CIwFVec2(0, 0), CIwFVec2(displayWidth / 2, displayHeight));
		if ((float)g_pInput->m_X >= displayWidth / 2) {
			Iw2DDrawImage(image_1, image_position);		// Draw an image
		}
		else Iw2DDrawImage(image_2, image_position);	// Draw an image
		/* Check for user tapping screen */
        if (g_pInput->m_Touched) {
            /* Move image to touched position */
            image_position.x = (float)g_pInput->m_X;
            image_position.y = (float)g_pInput->m_Y;
            //g_pInput->Reset();						// Reset input		
        }
		if (!g_pInput->m_Touched && g_pInput->m_PrevTouched) {
			image_position.x = (float)g_pInput->m_X;
			image_position.y = (float)g_pInput->m_Y;
			g_pInput->Reset();
		}
        Iw2DSurfaceShow();						// Show the drawing surface
        s3eDeviceYield(0);						// Yield to the OS
    }
    // Clean-up
    delete image_1;
	delete image_2;
    delete g_pInput;
    Iw2DTerminate();
    return 0;
}
