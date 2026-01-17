import { useEffect, useState } from 'react';
import { useFrame } from '@react-three/fiber';
import { Texture, LinearFilter, SRGBColorSpace } from 'three';

interface WebcamWallProps {
    width: number;
    height: number;
}

export function WebcamWall({ width, height }: WebcamWallProps) {
    const [texture, setTexture] = useState<Texture | null>(null);
    const [aspect, setAspect] = useState(1.77);

    useEffect(() => {
        // Create an Image element for MJPEG stream
        const img = new Image();
        img.crossOrigin = 'Anonymous';
        img.src = 'http://localhost:8000/video_feed';

        const tex = new Texture(img);
        tex.minFilter = LinearFilter;
        tex.magFilter = LinearFilter;
        tex.colorSpace = SRGBColorSpace;

        // MJPEG: Set texture immediately so it renders
        setTexture(tex);

        // Update aspect ratio when first frame arrives
        img.onload = () => {
            setAspect(img.width / img.height);
        };

        return () => {
            img.src = '';
            tex.dispose();
        };
    }, []);

    // Force texture update every frame to catch new MJPEG frames
    useFrame(() => {
        if (texture) {
            texture.needsUpdate = true;
        }
    });

    return (
        <group>
            {/* 1. The Black Base Wall (Fills the room height) */}
            <mesh rotation={[0, Math.PI, 0]}>
                <planeGeometry args={[width, height]} />
                <meshStandardMaterial color="#111" roughness={0.9} />
            </mesh>

            {/* 2. The Video Mesh (Sized to Aspect Ratio - Contain) */}
            {texture && (
                <mesh
                    rotation={[0, Math.PI, 0]}
                    position={[0, 0, -100]} /* Shift "Forward" into the room significantly */
                    scale={[-1, 1, 1]}
                >
                    <planeGeometry args={[
                        (aspect > width / height) ? width : height * aspect,
                        (aspect > width / height) ? width / aspect : height
                    ]} />
                    <meshBasicMaterial map={texture} toneMapped={false} />
                </mesh>
            )}
        </group>
    );
}
